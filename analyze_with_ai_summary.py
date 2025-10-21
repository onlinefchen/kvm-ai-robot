#!/usr/bin/env python3
"""
分析 kvmarm 邮件列表并使用 AI 生成 Thread 总结
支持双格式输出（Markdown + HTML）和历史归档
"""

import subprocess
import re
import os
import sys
from email import message_from_string
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta
from collections import defaultdict
from typing import Dict, List, Optional, Tuple
import argparse
import json


# 模型 token 限制配置
MODEL_LIMITS = {
    'gpt-4o-mini': {'input': 128000, 'safe_limit': 6000},
    'gpt-4o': {'input': 128000, 'safe_limit': 8000},
    'gpt-4': {'input': 8192, 'safe_limit': 3000},
    'claude-3-5-sonnet-20241022': {'input': 200000, 'safe_limit': 8000},
    'claude-3-opus-20240229': {'input': 200000, 'safe_limit': 8000},
    'claude-3-sonnet-20240229': {'input': 200000, 'safe_limit': 8000},
    'claude-3-haiku-20240307': {'input': 200000, 'safe_limit': 6000},
}


def estimate_tokens(text: str) -> int:
    """
    估算文本的 token 数量
    简单估算：英文约 4 字符/token，中文约 1.5 字符/token
    """
    # 统计中英文字符
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
    total_chars = len(text)
    english_chars = total_chars - chinese_chars

    # 估算 tokens
    estimated = (english_chars / 4) + (chinese_chars / 1.5)
    return int(estimated * 1.1)  # 加 10% 的安全边际


class Email:
    """邮件对象"""
    def __init__(self, commit_hash: str, email_msg: str):
        self.commit_hash = commit_hash
        self.msg = message_from_string(email_msg)

        self.message_id = self._clean_header(self.msg.get('Message-ID', ''))
        self.subject = self._clean_subject(self.msg.get('Subject', ''))
        self.raw_subject = self.msg.get('Subject', '')
        self.from_addr = self.msg.get('From', '')
        self.date_str = self.msg.get('Date', '')

        try:
            self.date = parsedate_to_datetime(self.date_str)
        except:
            self.date = None

        self.in_reply_to = self._clean_header(self.msg.get('In-Reply-To', ''))
        self.references = self._parse_references(self.msg.get('References', ''))
        self.body = self._extract_body()

    def _clean_header(self, header: str) -> str:
        return header.strip().strip('<>')

    def _clean_subject(self, subject: str) -> str:
        subject = re.sub(r'^(Re:\s*|Fwd:\s*)+', '', subject, flags=re.IGNORECASE)
        return subject.strip()

    def _parse_references(self, references: str) -> List[str]:
        if not references:
            return []
        return re.findall(r'<([^>]+)>', references)

    def _extract_body(self) -> str:
        body = ""
        if self.msg.is_multipart():
            for part in self.msg.walk():
                if part.get_content_type() == 'text/plain':
                    try:
                        payload = part.get_payload(decode=True)
                        if payload:
                            body = payload.decode('utf-8', errors='replace')
                            break
                    except:
                        pass
        else:
            try:
                payload = self.msg.get_payload(decode=True)
                if payload:
                    body = payload.decode('utf-8', errors='replace')
            except:
                body = str(self.msg.get_payload())
        return self._clean_body(body)

    def _clean_body(self, body: str) -> str:
        if not body:
            return ""
        lines = []
        for line in body.split('\n'):
            if line.strip().startswith('>'):
                continue
            if line.strip() in ['--', '_______________________________________________']:
                break
            lines.append(line)
        return '\n'.join(lines).strip()

    def get_thread_root(self) -> str:
        if self.in_reply_to:
            return self.in_reply_to
        elif self.references:
            return self.references[0]
        return self.message_id

    def get_author_name(self) -> str:
        match = re.match(r'^([^<]+)<', self.from_addr)
        if match:
            return match.group(1).strip().strip('"')
        match = re.search(r'<([^@>]+)@', self.from_addr)
        if match:
            return match.group(1)
        return self.from_addr

    def get_author_email(self) -> str:
        """提取邮箱地址"""
        match = re.search(r'<([^>]+)>', self.from_addr)
        if match:
            return match.group(1)
        # 如果没有尖括号，可能整个就是邮箱
        if '@' in self.from_addr:
            return self.from_addr
        return ""

    def get_author_with_email(self) -> str:
        """获取作者名称和邮箱的组合"""
        name = self.get_author_name()
        email = self.get_author_email()
        if email and email != name:
            return f"{name} <{email}>"
        return name


class AISummarizer:
    """AI 总结器基类"""
    def __init__(self, model: str = None):
        self.model = model

    def summarize_thread(self, thread_emails: List[Email]) -> str:
        raise NotImplementedError

    def _prepare_thread_content(self, thread_emails: List[Email]) -> Tuple[str, str]:
        """
        准备 thread 内容，包含所有邮件
        返回：(准备好的内容, 策略说明)
        """
        content = f"主题: {thread_emails[0].subject}\n"
        content += f"总邮件数: {len(thread_emails)}\n"
        content += f"参与者: {len(set(e.get_author_name() for e in thread_emails))}\n\n"

        # 包含所有邮件，不做任何截断
        for i, email in enumerate(thread_emails, 1):
            content += f"--- 邮件 {i}/{len(thread_emails)} - {email.get_author_name()} ---\n"
            body = email.body if email.body else "[无正文]"
            content += f"{body}\n\n"

        # 估算 token 数用于显示
        total_tokens = estimate_tokens(content)
        strategy = f"完整 thread ({total_tokens} tokens)"

        return content, strategy


class OpenAISummarizer(AISummarizer):
    """OpenAI API 总结器"""
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        super().__init__(model)
        self.api_key = api_key
        try:
            import openai
            self.client = openai.OpenAI(api_key=api_key)
        except ImportError:
            print("❌ 需要安装 openai 库: pip install openai")
            sys.exit(1)

    def summarize_thread(self, thread_emails: List[Email]) -> str:
        thread_content, strategy = self._prepare_thread_content(thread_emails)

        prompt = f"""请分析以下邮件列表 thread 的讨论内容，生成一个简洁的中文总结（200-300字）。

总结应包括：
1. 主要讨论的技术问题或补丁内容
2. 关键的技术要点
3. 主要的讨论结论或待解决的问题

Thread 内容：
{thread_content}

请用中文总结："""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一个专业的技术邮件列表分析助手，擅长总结 Linux 内核和虚拟化相关的技术讨论。"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.3
            )
            summary = response.choices[0].message.content.strip()
            return summary
        except Exception as e:
            return f"[AI 总结失败: {str(e)}]\n策略: {strategy}"


class AnthropicSummarizer(AISummarizer):
    """Anthropic Claude API 总结器"""
    def __init__(self, api_key: str, model: str = "claude-3-5-sonnet-20241022"):
        super().__init__(model)
        self.api_key = api_key
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=api_key)
        except ImportError:
            print("❌ 需要安装 anthropic 库: pip install anthropic")
            sys.exit(1)

    def summarize_thread(self, thread_emails: List[Email]) -> str:
        thread_content, strategy = self._prepare_thread_content(thread_emails)

        prompt = f"""请分析以下邮件列表 thread 的讨论内容，生成一个简洁的中文总结（200-300字）。

总结应包括：
1. 主要讨论的技术问题或补丁内容
2. 关键的技术要点和实现细节
3. 主要的讨论结论或待解决的问题
4. 如果有争议，简要说明不同观点

Thread 内容：
{thread_content}"""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=600,
                temperature=0.3,
                system="你是一个专业的技术邮件列表分析助手，擅长总结 Linux 内核、KVM 和 ARM 虚拟化相关的技术讨论。",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            summary = message.content[0].text.strip()
            return summary
        except Exception as e:
            return f"[AI 总结失败: {str(e)}]\n策略: {strategy}"


class RuleBasedSummarizer(AISummarizer):
    """基于规则的总结器（无需 API）"""
    def __init__(self):
        super().__init__(None)

    def summarize_thread(self, thread_emails: List[Email]) -> str:
        first = thread_emails[0]
        summary_parts = []

        # 基本信息
        summary_parts.append(f"本 thread 共有 {len(thread_emails)} 封邮件，{len(set(e.get_author_name() for e in thread_emails))} 位参与者。")

        # 识别类型
        if '[PATCH' in first.raw_subject:
            patch_desc = self._extract_patch_description(first)
            if patch_desc:
                summary_parts.append(f"\n\n📋 补丁内容：{patch_desc[:200]}...")
        elif '[RFC' in first.raw_subject:
            summary_parts.append("\n\n💭 这是一个征求意见（RFC）的讨论。")
        elif 'Question' in first.raw_subject or '?' in first.subject:
            summary_parts.append("\n\n❓ 这是一个技术问题讨论。")

        # 提取关键点（从所有邮件中）
        key_points = self._extract_key_points(thread_emails)
        if key_points:
            summary_parts.append("\n\n🔑 关键讨论点：")
            for point in key_points[:3]:
                summary_parts.append(f"\n• {point[:150]}...")

        # 讨论活跃度
        if len(thread_emails) > 15:
            summary_parts.append(f"\n\n💬 这是一个非常活跃的讨论，有 {len(thread_emails)} 封邮件往来。")
        elif len(thread_emails) > 5:
            summary_parts.append(f"\n\n💬 讨论有 {len(thread_emails)} 轮回复。")

        return ''.join(summary_parts)

    def _extract_patch_description(self, email: Email) -> Optional[str]:
        if not email.body:
            return None

        patterns = [
            r'(?:This patch|This series|This commit)\s+([^.]{20,200})',
            r'(?:Add|Fix|Update|Remove|Implement)\s+([^.]{20,200})',
        ]

        for pattern in patterns:
            match = re.search(pattern, email.body, re.IGNORECASE)
            if match:
                return match.group(0)

        paragraphs = [p.strip() for p in email.body.split('\n\n') if p.strip()]
        if paragraphs:
            first = paragraphs[0]
            if len(first) < 300:
                return first

        return None

    def _extract_key_points(self, thread_emails: List[Email]) -> List[str]:
        points = []

        for email in thread_emails[1:6]:
            if not email.body:
                continue

            questions = re.findall(r'([^.!?]{20,120}\?)', email.body)
            for q in questions[:2]:
                if len(q.strip()) > 25:
                    points.append(q.strip())

            lines = [line.strip() for line in email.body.split('\n')
                    if line.strip() and len(line.strip()) > 30]
            for line in lines[:2]:
                if any(kw in line.lower() for kw in ['should', 'need', 'must', 'important']):
                    if len(line) < 150:
                        points.append(line)

        return points[:5]


class ThreadAnalyzer:
    """Thread 分析器（支持双格式输出）"""
    def __init__(self, git_dir: str, days: int, summarizer: AISummarizer, since: str = None, until: str = None):
        self.git_dir = git_dir
        self.days = days
        self.since = since
        self.until = until
        self.summarizer = summarizer
        self.emails: Dict[str, Email] = {}

    def fetch_emails(self):
        # 优先使用 since/until，否则使用 days
        if self.since and self.until:
            print(f"正在获取 {self.since} 至 {self.until} 的邮件...")
            cmd = ['git', f'--git-dir={self.git_dir}', 'log', '--all',
                   f'--since={self.since} 00:00:00', f'--until={self.until} 23:59:59', '--format=%H']
        else:
            print(f"正在获取最近 {self.days} 天的邮件...")
            cmd = ['git', f'--git-dir={self.git_dir}', 'log',
                   f'--since={self.days} days ago', '--format=%H']

        result = subprocess.run(cmd, capture_output=True, text=True)
        commits = result.stdout.strip().split('\n')

        print(f"找到 {len(commits)} 封邮件")

        for i, commit in enumerate(commits, 1):
            if i % 20 == 0:
                print(f"  处理进度: {i}/{len(commits)}")

            cmd = ['git', f'--git-dir={self.git_dir}', 'show', f'{commit}:m']
            result = subprocess.run(cmd, capture_output=True)

            if result.returncode == 0:
                try:
                    email_text = result.stdout.decode('utf-8')
                except UnicodeDecodeError:
                    email_text = result.stdout.decode('utf-8', errors='replace')

                email = Email(commit, email_text)
                if email.message_id:
                    self.emails[email.message_id] = email

        print(f"成功解析 {len(self.emails)} 封邮件\n")

    def build_threads(self) -> Dict[str, List[Email]]:
        print("正在构建 thread 结构...")
        threads = defaultdict(list)

        for email in self.emails.values():
            root_id = email.get_thread_root()
            visited = set()
            while root_id in self.emails and root_id not in visited:
                visited.add(root_id)
                parent = self.emails[root_id]
                parent_root = parent.get_thread_root()
                if parent_root == root_id:
                    break
                root_id = parent_root
            threads[root_id].append(email)

        for thread_id in threads:
            threads[thread_id].sort(key=lambda e: e.date if e.date else datetime.min.replace(tzinfo=timezone.utc))

        print(f"找到 {len(threads)} 个不同的 thread\n")
        return threads

    def categorize_threads(self, threads: Dict[str, List[Email]]) -> Dict[str, List[tuple]]:
        categories = {
            'PATCH': [], 'RFC': [], 'Bug Report': [], 'Selftest': [],
            'Question': [], 'GIT PULL': [], 'Discussion': [], 'Other': []
        }

        for thread_id, thread_emails in threads.items():
            first = thread_emails[0]
            raw_subject = first.raw_subject
            subject = first.subject

            if '[PATCH' in raw_subject:
                category = 'PATCH'
            elif '[RFC' in raw_subject:
                category = 'RFC'
            elif '[GIT PULL]' in raw_subject:
                category = 'GIT PULL'
            elif 'selftest' in subject.lower():
                category = 'Selftest'
            elif any(w in subject.lower() for w in ['bug', 'issue', 'error', 'fail']):
                category = 'Bug Report'
            elif '[Question]' in raw_subject or subject.lower().startswith('question'):
                category = 'Question'
            elif 'Re:' in raw_subject:
                category = 'Discussion'
            else:
                category = 'Other'

            categories[category].append((thread_id, thread_emails))

        for cat in categories:
            categories[cat].sort(key=lambda x: len(x[1]), reverse=True)

        return categories

    def _scan_existing_week_reports(self, output_dir: str = 'docs') -> set:
        """扫描输出目录下已存在的周报告文件"""
        existing_files = set()

        # 确保目录存在
        if not os.path.exists(output_dir):
            return existing_files

        # 扫描输出目录
        for filename in os.listdir(output_dir):
            # 匹配格式：kvmarm_YYYY_weekWW.html
            match = re.match(r'kvmarm_(\d{4})_week(\d{2})\.html', filename)
            if match:
                year = int(match.group(1))
                week = int(match.group(2))
                existing_files.add((year, week))

        return existing_files

    def _generate_week_calendar(self, current_year: int, current_week: int, output_dir: str = '.') -> str:
        """生成全年月度周历HTML"""
        # 扫描已存在的报告文件
        existing_reports = self._scan_existing_week_reports()

        calendar_html = '<div class="year-calendar">\n'
        calendar_html += f'<h3 class="year-title">{current_year} 年度周历</h3>\n'
        calendar_html += '<div class="months-container">\n'

        # 遍历12个月
        for month in range(1, 13):
            # 获取该月第一天和最后一天
            first_day = datetime(current_year, month, 1)
            if month == 12:
                last_day = datetime(current_year, 12, 31)
            else:
                last_day = datetime(current_year, month + 1, 1) - timedelta(days=1)

            # 获取该月的所有周
            month_weeks = []
            current_date = first_day

            while current_date <= last_day:
                year, week, weekday = current_date.isocalendar()
                if year == current_year and (year, week) not in [(y, w) for y, w, _, _ in month_weeks]:
                    monday = datetime.fromisocalendar(year, week, 1)
                    sunday = datetime.fromisocalendar(year, week, 7)
                    month_weeks.append((year, week, monday, sunday))
                current_date += timedelta(days=7)

            if not month_weeks:
                continue

            # 月份标题
            calendar_html += f'<div class="month-section">\n'
            calendar_html += f'  <div class="month-title">{month}月</div>\n'
            calendar_html += f'  <div class="month-weeks">\n'

            # 该月的所有周
            for year, week, monday, sunday in month_weeks:
                filename = f"kvmarm_{year}_week{week:02d}.html"
                file_exists = (year, week) in existing_reports
                is_current = (year == current_year and week == current_week)

                # 设置CSS类
                if is_current:
                    css_class = "week-item current-week"
                elif file_exists:
                    css_class = "week-item week-available"
                else:
                    css_class = "week-item week-unavailable"

                # 只有存在的文件才是链接
                if file_exists or is_current:
                    calendar_html += f'    <a href="{filename}" class="{css_class}">\n'
                else:
                    calendar_html += f'    <span class="{css_class}">\n'

                calendar_html += f'      <div class="week-number">W{week}</div>\n'
                calendar_html += f'      <div class="week-date">{monday.strftime("%m/%d")}-{sunday.strftime("%m/%d")}</div>\n'

                if file_exists or is_current:
                    calendar_html += f'    </a>\n'
                else:
                    calendar_html += f'    </span>\n'

            calendar_html += f'  </div>\n'
            calendar_html += f'</div>\n'

        calendar_html += '</div>\n'  # 结束 months-container
        calendar_html += '</div>\n'  # 结束 year-calendar
        return calendar_html

    def generate_archive_page(self, output_dir: str = 'docs'):
        """生成历史归档页面"""
        print("正在生成历史归档页面...")

        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)

        # 扫描已存在的报告文件
        existing_reports = self._scan_existing_week_reports(output_dir)

        # 按年份和周次排序
        sorted_reports = sorted(existing_reports, key=lambda x: (x[0], x[1]), reverse=True)

        # 按年份分组
        reports_by_year = defaultdict(list)
        for year, week in sorted_reports:
            reports_by_year[year].append(week)

        # 生成HTML
        html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KVMARM 邮件列表历史归档</title>
    <style>
        body {
            font-family: 'Courier New', 'Courier', monospace;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 30px 40px;
            background-color: #ffffff;
            color: #222;
        }
        h1 {
            font-size: 2.2em;
            font-weight: bold;
            color: #000;
            margin-bottom: 0.5em;
            text-align: center;
            border-bottom: 2px solid #000;
            padding-bottom: 15px;
        }
        .year-section {
            margin: 30px 0;
            border: 2px solid #333;
            background: #fafafa;
        }
        .year-header {
            background: #333;
            color: #fff;
            padding: 12px 20px;
            font-size: 1.5em;
            font-weight: bold;
        }
        .weeks-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            padding: 20px;
        }
        .week-link {
            display: block;
            text-decoration: none;
            padding: 12px 15px;
            background: #fff;
            border: 2px solid #666;
            text-align: center;
            color: #000;
            transition: all 0.2s;
            min-width: 120px;
        }
        .week-link:hover {
            background: #000;
            color: #fff;
            border-color: #000;
            transform: translateY(-3px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }
        .week-number {
            font-size: 1.1em;
            font-weight: bold;
            margin-bottom: 4px;
        }
        .week-date {
            font-size: 0.9em;
            color: #666;
        }
        .week-link:hover .week-date {
            color: #ccc;
        }
        .meta-info {
            background: #f5f5f5;
            border: 1px solid #ccc;
            padding: 15px 20px;
            margin: 20px 0;
            text-align: center;
            font-size: 0.95em;
        }
    </style>
</head>
<body>
    <h1>KVMARM Mailing List Archive</h1>
    <div class="meta-info">
        <p><strong>Generated:</strong> """ + datetime.now().strftime('%Y-%m-%d %H:%M') + """</p>
        <p><strong>Total Reports:</strong> """ + str(len(sorted_reports)) + """</p>
    </div>
"""

        # 为每个年份生成一个section
        for year in sorted(reports_by_year.keys(), reverse=True):
            weeks = sorted(reports_by_year[year], reverse=True)
            html_content += f"""
    <div class="year-section">
        <div class="year-header">{year} 年</div>
        <div class="weeks-grid">
"""
            for week in weeks:
                filename = f"kvmarm_{year}_week{week:02d}.html"
                monday = datetime.fromisocalendar(year, week, 1)
                sunday = datetime.fromisocalendar(year, week, 7)

                html_content += f"""            <a href="{filename}" class="week-link">
                <div class="week-number">第 {week} 周</div>
                <div class="week-date">{monday.strftime('%m/%d')} - {sunday.strftime('%m/%d')}</div>
            </a>
"""

            html_content += """        </div>
    </div>
"""

        html_content += """
</body>
</html>
"""

        # 写入文件
        archive_file = os.path.join(output_dir, 'archive.html')
        with open(archive_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✅ 历史归档页面已生成: {archive_file}")
        return archive_file

    def generate_html_report(self, categories: Dict[str, List[tuple]], output_file: str):
        """生成 HTML 格式报告"""
        print("正在生成 HTML 报告...")

        total_threads = sum(len(threads) for threads in categories.values())
        total_emails = sum(len(emails) for _, emails in
                          sum(categories.values(), []))
        large_threads = sum(1 for _, emails in sum(categories.values(), []) if len(emails) > 20)

        # 从文件名中提取周信息（如果是标准格式）
        # 格式：kvmarm_YYYY_weekWW.html
        basename = os.path.basename(output_file)
        week_match = re.match(r'kvmarm_(\d{4})_week(\d{2})\.html', basename)

        if week_match:
            # 从文件名提取周信息
            year = int(week_match.group(1))
            week_num = int(week_match.group(2))
        else:
            # 使用当前周信息
            now = datetime.now()
            year, week_num, weekday = now.isocalendar()

        # 计算这一周的日期范围
        monday = datetime.fromisocalendar(year, week_num, 1)
        sunday = datetime.fromisocalendar(year, week_num, 7)

        html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KVMARM 邮件列表 AI 总结报告</title>
    <style>
        body {{
            font-family: 'Courier New', 'Courier', monospace;
            line-height: 1.5;
            max-width: 1200px;
            margin: 0 auto;
            padding: 30px 40px;
            background-color: #ffffff;
            color: #222;
        }}
        .container {{
            background: #ffffff;
        }}
        h1 {{
            font-size: 2.2em;
            font-weight: bold;
            color: #000;
            margin-bottom: 0.3em;
            text-align: center;
            border-bottom: 2px solid #000;
            padding-bottom: 15px;
        }}
        h2 {{
            font-size: 1.6em;
            font-weight: bold;
            color: #000;
            margin-top: 2em;
            margin-bottom: 0.6em;
            border-bottom: 1px solid #333;
            padding-bottom: 8px;
        }}
        h3 {{
            font-size: 1.2em;
            font-weight: bold;
            color: #111;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }}
        h4 {{
            font-size: 1.05em;
            font-weight: bold;
            color: #333;
            margin-top: 1.2em;
            margin-bottom: 0.5em;
        }}
        .meta-info {{
            background: #f9f9f9;
            border: 1px solid #ddd;
            padding: 15px 20px;
            margin: 20px 0;
            font-size: 0.95em;
            line-height: 1.6;
        }}
        .meta-info p {{
            margin: 6px 0;
            color: #444;
        }}
        .meta-info strong {{
            color: #000;
            font-weight: bold;
        }}
        .stats {{
            display: table;
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            border: 1px solid #000;
        }}
        .stat-card {{
            display: table-cell;
            border: 1px solid #000;
            padding: 12px 15px;
            text-align: center;
            background: #fafafa;
        }}
        .stat-card h3 {{
            margin: 0;
            color: #000;
            font-size: 1.8em;
            font-weight: bold;
            border: none;
            padding: 0;
        }}
        .stat-card p {{
            margin: 5px 0 0 0;
            color: #444;
            font-size: 0.9em;
            font-weight: normal;
        }}
        .category {{
            margin: 30px 0;
        }}
        .thread {{
            margin: 25px 0;
            padding: 15px;
            background: #fafafa;
            border: 1px solid #ccc;
            page-break-inside: avoid;
        }}
        .thread-header {{
            margin-bottom: 12px;
            border-bottom: 1px solid #ddd;
            padding-bottom: 10px;
        }}
        .thread-header h3 {{
            font-size: 1.15em;
            font-weight: bold;
            color: #000;
            margin: 0;
        }}
        .thread-meta {{
            display: block;
            margin: 8px 0 12px 0;
            font-size: 0.9em;
            color: #555;
            font-style: italic;
        }}
        .thread-meta span {{
            margin-right: 15px;
        }}
        .ai-summary {{
            background: #fff;
            border-left: 3px solid #666;
            padding: 12px 15px;
            margin: 15px 0;
            line-height: 1.6;
            color: #222;
            font-style: italic;
        }}
        .email-list {{
            background: #fff;
            border: 1px solid #ccc;
            padding: 10px 15px;
            font-family: 'Courier New', 'Consolas', monospace;
            font-size: 0.88em;
            line-height: 1.5;
            overflow-x: auto;
            margin: 10px 0;
        }}
        .email-item {{
            margin: 4px 0;
            padding: 2px 0;
            color: #222;
        }}
        .email-date {{
            color: #0066cc;
            font-weight: bold;
        }}
        .email-sender {{
            color: #c30;
            font-weight: normal;
        }}
        .email-subject {{
            color: #000;
        }}
        .archive-link {{
            display: inline-block;
            margin: 15px 0;
            padding: 10px 20px;
            background: #333;
            color: #fff;
            text-decoration: none;
            border: 2px solid #000;
            font-weight: bold;
            transition: all 0.2s;
        }}
        .archive-link:hover {{
            background: #000;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>KVMARM Mailing List Analysis Report</h1>

        <div class="meta-info">
            <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
            <p><strong>Time Period:</strong> {year}年{monday.month}月 第{week_num}周 ({monday.strftime('%m/%d')} - {sunday.strftime('%m/%d')})</p>
            <p><strong>Total Messages:</strong> {total_emails} | <strong>Total Threads:</strong> {total_threads}</p>
            <p style="text-align: center;"><a href="archive.html" class="archive-link">📚 历史归档 Archive</a></p>
        </div>

"""

        # 每个分类的详细内容
        for category, threads in categories.items():
            if not threads:
                continue

            html_content += f"""
        <div class="category">
            <h2>{category}</h2>
"""

            for i, (thread_id, thread_emails) in enumerate(threads, 1):
                first = thread_emails[0]

                summary = self.summarizer.summarize_thread(thread_emails)
                summary_html = summary.replace('\n', '<br>')

                html_content += f"""
            <div class="thread">
                <div class="thread-header">
                    <h3>{first.subject}</h3>
                </div>

                <div class="thread-meta">
                    <span>{len(thread_emails)} messages</span>
                    <span>{len(set(e.get_author_name() for e in thread_emails))} participants</span>
                    <span>Started: {first.date.strftime('%Y-%m-%d') if first.date else 'N/A'}</span>
                </div>

                <div class="ai-summary">
                    {summary_html}
                </div>

                <h4>Message List</h4>
                <div class="email-list">
"""

                for j, email in enumerate(thread_emails, 1):
                    author_name = email.get_author_name()
                    author_email = email.get_author_email()
                    date = email.date.strftime('%Y-%m-%d') if email.date else 'N/A'
                    html_content += f"""<div class="email-item"><span class="email-date">[{date}]</span> <span class="email-subject">{email.raw_subject}</span><br>&nbsp;&nbsp;&nbsp;&nbsp;Author: {author_name} <span class="email-sender">&lt;{author_email}&gt;</span></div>
"""

                html_content += """                </div>
            </div>
"""

            html_content += "        </div>\n"

        html_content += """
    </div>
</body>
</html>
"""

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✅ HTML 报告已生成: {output_file}")

    def generate_report(self, categories: Dict[str, List[tuple]], output_file: str):
        print("正在生成 AI 总结报告...\n")

        total_threads = sum(len(threads) for threads in categories.values())
        total_emails = sum(len(emails) for _, emails in
                          sum(categories.values(), []))

        # 统计大型 threads
        large_threads = sum(1 for _, emails in sum(categories.values(), []) if len(emails) > 20)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# KVMARM 邮件列表 AI 总结报告\n\n")
            f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**分析周期**: 最近 {self.days} 天\n\n")

            # 总体统计
            f.write("## 📊 总体统计\n\n")
            f.write(f"- **总邮件数**: {total_emails}\n")
            f.write(f"- **总 Thread 数**: {total_threads}\n")
            if large_threads > 0:
                f.write(f"- **大型 Thread** (>20封): {large_threads} 个\n")
            f.write("\n")

            # 分类统计
            f.write("### 分类分布\n\n")
            for category, threads in categories.items():
                if threads:
                    email_count = sum(len(emails) for _, emails in threads)
                    f.write(f"- **{category}**: {len(threads)} threads ({email_count} 邮件)\n")
            f.write("\n---\n\n")

            # 每个分类的详细 thread
            for category, threads in categories.items():
                if not threads:
                    continue

                f.write(f"## 📌 {category}\n\n")
                f.write(f"共 {len(threads)} 个 thread\n\n")
                f.write("---\n\n")

                for i, (thread_id, thread_emails) in enumerate(threads, 1):
                    first = thread_emails[0]

                    # 显示处理进度
                    print(f"  正在总结 {category} thread {i}/{len(threads)}: {first.subject[:40]}...")

                    # Thread 章节标题
                    f.write(f"### Thread {i}: {first.subject}\n\n")

                    # 基本信息
                    f.write(f"**📧 邮件数**: {len(thread_emails)} | ")
                    f.write(f"**👥 参与者**: {len(set(e.get_author_name() for e in thread_emails))} | ")
                    f.write(f"**📅 开始时间**: {first.date_str}\n\n")

                    # AI 总结
                    f.write("#### 🤖 AI 总结\n\n")
                    summary = self.summarizer.summarize_thread(thread_emails)
                    f.write(f"{summary}\n\n")

                    # 邮件标题列表
                    f.write("#### 📝 邮件列表\n\n")
                    for j, email in enumerate(thread_emails, 1):
                        author = email.get_author_with_email()
                        date = email.date.strftime('%m-%d %H:%M') if email.date else 'N/A'
                        f.write(f"{j}. **[{date}]** {email.raw_subject}\n")
                        f.write(f"   - 发件人: {author}\n")

                    f.write("\n---\n\n")

        print(f"\n✅ 报告已生成: {output_file}")
        print(f"📊 处理了 {total_threads} 个 thread，共 {total_emails} 封邮件")


def generate_week_report(year: int, week: int, monday: str, sunday: str,
                         git_dir: str, summarizer: AISummarizer, output_dir: str):
    """生成单周报告"""
    # 检查邮件数量
    cmd = ['git', f'--git-dir={git_dir}', 'log', '--all',
           f'--since={monday} 00:00:00', f'--until={sunday} 23:59:59',
           '--oneline']
    result = subprocess.run(cmd, capture_output=True, text=True)
    email_count = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0

    if email_count == 0:
        return 'skip_empty'

    print(f"📧 邮件数量: {email_count}")

    # 输出文件
    base_name = f"kvmarm_{year}_week{week:02d}"
    md_file = os.path.join(output_dir, f"{base_name}.md")
    html_file = os.path.join(output_dir, f"{base_name}.html")

    # 运行分析
    analyzer = ThreadAnalyzer(git_dir, 7, summarizer, monday, sunday)
    analyzer.fetch_emails()
    threads = analyzer.build_threads()
    categories = analyzer.categorize_threads(threads)

    # 生成两种格式的报告
    analyzer.generate_report(categories, md_file)
    analyzer.generate_html_report(categories, html_file)

    # 生成归档页面
    analyzer.generate_archive_page(output_dir)

    return 'success'


def main():
    parser = argparse.ArgumentParser(
        description='KVMARM 邮件列表周报告生成器',
        epilog='''
示例:
  %(prog)s                                    # 生成本周报告
  %(prog)s --start 2025-01-01                # 从2025年初到现在
  %(prog)s --start 2025-01-01 --end 2025-03-31  # 第一季度
  %(prog)s --ai openai --model gpt-4o-mini   # 使用 OpenAI
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # 日期范围参数
    parser.add_argument('--start', type=str,
                       help='起始日期 (格式: YYYY-MM-DD)，将生成该日期所在周到结束日期所在周的所有报告')
    parser.add_argument('--end', type=str,
                       help='结束日期 (格式: YYYY-MM-DD，默认为今天)')

    # 保留兼容性参数（用于单周生成）
    parser.add_argument('-d', '--days', type=int, default=7,
                       help=argparse.SUPPRESS)  # 隐藏，仅内部使用
    parser.add_argument('--since', type=str,
                       help=argparse.SUPPRESS)  # 隐藏，仅内部使用
    parser.add_argument('--until', type=str,
                       help=argparse.SUPPRESS)  # 隐藏，仅内部使用

    # 其他参数
    parser.add_argument('-o', '--output', type=str,
                       help='输出文件路径（不含扩展名）')
    parser.add_argument('--git-dir', type=str,
                       default='git/0.git',
                       help='Git 仓库路径 (默认: git/0.git)')
    parser.add_argument('--ai', type=str, choices=['openai', 'claude', 'none'],
                       default='none',
                       help='AI 后端: openai, claude, 或 none (默认: none)')
    parser.add_argument('--api-key', type=str,
                       help='API Key (可通过环境变量设置)')
    parser.add_argument('--model', type=str,
                       help='AI 模型名称')

    args = parser.parse_args()

    # 选择总结器
    if args.ai == 'openai':
        api_key = args.api_key or os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ 需要设置 OPENAI_API_KEY 环境变量或使用 --api-key")
            sys.exit(1)
        model = args.model or 'gpt-4o-mini'
        summarizer = OpenAISummarizer(api_key, model)
        print(f"✅ 使用 OpenAI {model}")
    elif args.ai == 'claude':
        api_key = args.api_key or os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            print("❌ 需要设置 ANTHROPIC_API_KEY 环境变量或使用 --api-key")
            sys.exit(1)
        model = args.model or 'claude-3-5-sonnet-20241022'
        summarizer = AnthropicSummarizer(api_key, model)
        print(f"✅ 使用 Anthropic Claude {model}")
    else:
        summarizer = RuleBasedSummarizer()
        print("✅ 使用基于规则的总结（无需 API）")

    # 确保输出目录存在
    output_dir = 'docs'
    os.makedirs(output_dir, exist_ok=True)

    # 判断是批量模式还是单周模式
    if args.start:
        # 批量模式：生成日期范围内的所有周
        print("=" * 50)
        print("KVMARM 邮件列表周报告批量生成")
        print("=" * 50)
        print()

        # 计算日期范围
        start_date = datetime.strptime(args.start, "%Y-%m-%d")
        end_date = datetime.strptime(args.end, "%Y-%m-%d") if args.end else datetime.now()

        # 获取 start 所在周和 end 所在周
        start_year, start_week, _ = start_date.isocalendar()
        end_year, end_week, _ = end_date.isocalendar()

        # 获取当前周信息（用于判断是否覆盖）
        now = datetime.now()
        current_year, current_week, _ = now.isocalendar()

        print(f"📅 日期范围: {args.start} 到 {end_date.strftime('%Y-%m-%d')}")
        print(f"📅 周范围: {start_year}年第{start_week}周 到 {end_year}年第{end_week}周")
        print()

        # 生成需要处理的周列表
        weeks_to_process = []
        year, week = start_year, start_week

        while True:
            monday = datetime.fromisocalendar(year, week, 1)
            sunday = datetime.fromisocalendar(year, week, 7)
            weeks_to_process.append((year, week, monday.strftime('%Y-%m-%d'), sunday.strftime('%Y-%m-%d')))

            if year == end_year and week == end_week:
                break

            week += 1
            # 检查是否需要进入下一年
            try:
                datetime.fromisocalendar(year, week, 1)
            except ValueError:
                year += 1
                week = 1

        # 统计变量
        total_weeks = len(weeks_to_process)
        success_count = 0
        skip_count = 0
        fail_count = 0

        # 处理每一周
        import time
        for idx, (year, week, monday, sunday) in enumerate(weeks_to_process, 1):
            print("=" * 50)
            print(f"[{idx}/{total_weeks}] {year}年第{week}周")
            print("=" * 50)
            print(f"📅 日期范围: {monday} 到 {sunday}")

            # 判断是否为当前周
            is_current_week = (year == current_year and week == current_week)

            # 检查文件是否已存在
            base_name = f"kvmarm_{year}_week{week:02d}"
            md_file = os.path.join(output_dir, f"{base_name}.md")
            html_file = os.path.join(output_dir, f"{base_name}.html")

            if os.path.exists(md_file) and os.path.exists(html_file):
                if not is_current_week:
                    print("ℹ️  历史报告已存在，跳过")
                    skip_count += 1
                    print()
                    continue
                else:
                    print("🔄 当前周报告已存在，将重新生成")

            # 生成报告
            try:
                result = generate_week_report(year, week, monday, sunday,
                                              args.git_dir, summarizer, output_dir)
                if result == 'skip_empty':
                    print("ℹ️  该周没有邮件，跳过")
                    skip_count += 1
                else:
                    print(f"✅ {year}年第{week}周报告生成完成")
                    success_count += 1

                    # API 调用间隔
                    if args.ai != 'none' and idx < total_weeks:
                        print("⏳ 等待 3 秒避免 API 速率限制...")
                        time.sleep(3)

            except Exception as e:
                print(f"❌ {year}年第{week}周报告生成失败: {e}")
                fail_count += 1

            print()

        # 输出统计
        print("=" * 50)
        print("🎉 批量生成完成！")
        print("=" * 50)
        print()
        print("📊 生成统计：")
        print(f"   总周数: {total_weeks}")
        print(f"   成功: {success_count}")
        print(f"   跳过: {skip_count}")
        print(f"   失败: {fail_count}")
        print()
        html_count = len([f for f in os.listdir(output_dir) if f.endswith('.html') and f != 'archive.html'])
        md_count = len([f for f in os.listdir(output_dir) if f.endswith('.md')])
        print(f"📁 生成的报告位于 {output_dir}/ 目录：")
        print(f"   HTML 文件: {html_count}")
        print(f"   Markdown 文件: {md_count}")
        print()
        print(f"🌐 查看归档页面: {output_dir}/archive.html")

    else:
        # 单周模式（兼容旧版本或单次运行）
        if args.since and args.until:
            # 使用指定的日期范围
            monday = args.since
            sunday = args.until
        else:
            # 默认：生成本周报告
            now = datetime.now()
            year, week, _ = now.isocalendar()
            monday = datetime.fromisocalendar(year, week, 1).strftime('%Y-%m-%d')
            sunday = datetime.fromisocalendar(year, week, 7).strftime('%Y-%m-%d')

        print("=" * 50)
        print("KVMARM 邮件列表周报告生成")
        print("=" * 50)
        print()

        # 计算周信息
        monday_dt = datetime.strptime(monday, "%Y-%m-%d")
        year, week, _ = monday_dt.isocalendar()

        print(f"📅 {year}年第{week}周 ({monday} 到 {sunday})")
        print()

        # 输出文件
        if args.output:
            base_name = args.output.rsplit('.', 1)[0]  # 移除扩展名
            md_file = f"{base_name}.md"
            html_file = f"{base_name}.html"
        else:
            base_name = f"kvmarm_{year}_week{week:02d}"
            md_file = os.path.join(output_dir, f"{base_name}.md")
            html_file = os.path.join(output_dir, f"{base_name}.html")

        # 生成报告
        try:
            result = generate_week_report(year, week, monday, sunday,
                                          args.git_dir, summarizer, output_dir)
            if result == 'skip_empty':
                print("ℹ️  该周没有邮件")
                sys.exit(0)

            print()
            print(f"🎉 完成！生成了两种格式的报告：")
            print(f"   📄 Markdown: {md_file}")
            print(f"   🌐 HTML: {html_file}")
            print(f"   📚 Archive: {os.path.join(output_dir, 'archive.html')}")

        except Exception as e:
            print(f"❌ 报告生成失败: {e}")
            sys.exit(1)


if __name__ == '__main__':
    main()
