from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime

def generate_report(url, cms_info, users, login_pages, output_dir="output"):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report.html')

    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    output = template.render(
        target=url,
        cms=cms_info,
        users=users,
        logins=login_pages,
        timestamp=timestamp
    )

    with open(os.path.join(output_dir, "report.html"), "w") as f:
        f.write(output)
