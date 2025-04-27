import os
from datetime import datetime

def generate_report(summaries):
    today = datetime.now().strftime("%Y-%m-%d")
    output_path = f"outputs/digest-{today}.md"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# Daily Digest - {today}\n\n")
        for summary in summaries:
            f.write(f"## [{summary['title']}]({summary['link']})\n")
            f.write(f"*Topic: {summary['topic']}*\n\n")
            f.write(f"{summary['summary']}\n\n")
    print(f"Digest created: {output_path}")