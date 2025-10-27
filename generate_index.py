#!/usr/bin/env python3
"""生成 index.html 重定向到最新周报告"""

from datetime import datetime
import os
import re
import glob

# 查找 docs 目录下最新的周报文件
def find_latest_report():
    """查找最新的周报告文件"""
    pattern = os.path.join('docs', 'kvmarm_*_week*.html')
    files = glob.glob(pattern)

    if not files:
        # 如果没有找到文件，默认使用当前周
        now = datetime.now()
        year, week, _ = now.isocalendar()
        return f"kvmarm_{year}_week{week:02d}.html", year, week

    # 提取年份和周数，找到最新的
    latest_file = None
    latest_year = 0
    latest_week = 0

    for file in files:
        basename = os.path.basename(file)
        match = re.match(r'kvmarm_(\d{4})_week(\d{2})\.html', basename)
        if match:
            year = int(match.group(1))
            week = int(match.group(2))
            if year > latest_year or (year == latest_year and week > latest_week):
                latest_year = year
                latest_week = week
                latest_file = basename

    return latest_file if latest_file else f"kvmarm_{datetime.now().year}_week{datetime.now().isocalendar()[1]:02d}.html", latest_year, latest_week

# 获取最新周报文件
current_week_file, year, week = find_latest_report()

html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KVMARM Mailing List - Latest Week</title>
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
        // 自动重定向到最新周报告
        window.onload = function() {{
            // 3秒后自动跳转到最新报告
            setTimeout(() => {{
                window.location.href = "{current_week_file}";
            }}, 3000);
        }};
    </script>
</head>
<body>
    <div class="container">
        <h1>KVMARM Mailing List</h1>
        <p>Redirecting to latest week report in 3 seconds...</p>
        <div class="links">
            <a href="{current_week_file}">📅 Latest Week ({year} Week {week})</a>
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

print(f"✅ Created index.html redirecting to latest report: {current_week_file} ({year} Week {week})")
