#!/usr/bin/env python3
"""生成 index.html 重定向到当前周报告"""

from datetime import datetime
import os

# 获取当前周信息
now = datetime.now()
year, week, _ = now.isocalendar()
current_week_file = f"kvmarm_{year}_week{week:02d}.html"

html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KVMARM Mailing List - Current Week</title>
    <style>
        body {{
            font-family: 'Courier New', monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: #f5f5f5;
        }}
        .container {{
            text-align: center;
            padding: 40px;
            background: white;
            border: 2px solid #333;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        h1 {{
            font-size: 2em;
            margin-bottom: 20px;
            color: #000;
        }}
        p {{
            font-size: 1.2em;
            color: #666;
            margin-bottom: 30px;
        }}
        .links {{
            margin-top: 30px;
        }}
        a {{
            display: inline-block;
            margin: 10px;
            padding: 12px 24px;
            background: #333;
            color: white;
            text-decoration: none;
            border: 2px solid #333;
            transition: all 0.3s;
        }}
        a:hover {{
            background: #000;
            transform: translateY(-2px);
        }}
    </style>
    <script>
        // 自动重定向到当前周
        window.onload = function() {{
            const now = new Date();
            const year = now.getFullYear();

            // 计算 ISO 周数（简化版）
            const startOfYear = new Date(year, 0, 1);
            const days = Math.floor((now - startOfYear) / (24 * 60 * 60 * 1000));
            const week = Math.ceil((days + startOfYear.getDay() + 1) / 7);

            const weekStr = week.toString().padStart(2, '0');
            const currentWeekFile = `kvmarm_${{year}}_week${{weekStr}}.html`;

            // 更新显示
            document.getElementById('current-week-text').textContent = `${{year}} Week ${{week}}`;
            document.getElementById('current-week-link').href = currentWeekFile;

            // 3秒后自动跳转
            setTimeout(() => {{
                window.location.href = currentWeekFile;
            }}, 3000);
        }};
    </script>
</head>
<body>
    <div class="container">
        <h1>KVMARM Mailing List</h1>
        <p>Redirecting to current week report in 3 seconds...</p>
        <div class="links">
            <a id="current-week-link" href="{current_week_file}">📅 Current Week ({year} Week {week})</a>
            <a href="archive.html">📚 Archive</a>
        </div>
    </div>
</body>
</html>
"""

# 确保 docs 目录存在
os.makedirs('docs', exist_ok=True)

# 写入 index.html
with open('docs/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ Created index.html redirecting to {current_week_file}")
