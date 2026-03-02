# generate_site.py
import os
from datetime import datetime

REPORT_FILE = "final_report.txt"
SITE_DIR = "site"
OUTPUT_FILE = os.path.join(SITE_DIR, "index.html")


def generate_html(content):
    today = datetime.utcnow().strftime("%d %B %Y")

    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Daily News - {today}</title>

<style>
body {{
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #f7f7f7;
    margin: 0;
    padding: 20px;
    line-height: 1.6;
}}

.container {{
    max-width: 800px;
    margin: auto;
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}}

h1 {{
    text-align: center;
}}

pre {{
    white-space: pre-wrap;
    font-size: 15px;
}}

.footer {{
    margin-top: 30px;
    text-align: center;
    font-size: 12px;
    color: gray;
}}
</style>
</head>

<body>
<div class="container">
<h1>📰 Daily News Summary</h1>
<p style="text-align:center; color:gray;">{today}</p>

<pre>
{content}
</pre>

<div class="footer">
Generated automatically via GitHub Actions
</div>
</div>
</body>
</html>
"""


if __name__ == "__main__":
    if not os.path.exists(SITE_DIR):
        os.makedirs(SITE_DIR)

    with open(REPORT_FILE, "r") as f:
        content = f.read()

    html_content = generate_html(content)

    with open(OUTPUT_FILE, "w") as f:
        f.write(html_content)