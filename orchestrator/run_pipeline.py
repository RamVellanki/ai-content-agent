import os
from datetime import datetime
from agent.digest_agent import run_digest_pipeline

def save_digest_to_markdown(digest_entries):
    today = datetime.now().strftime("%Y-%m-%d")
    output_folder = "outputs"
    os.makedirs(output_folder, exist_ok=True)
    output_path = f"{output_folder}/digest-{today}.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# 📚 AI Digest - {today}\n\n")

        for entry in digest_entries:
            f.write(f"## [{entry['title']}]({entry['link']})\n")
            f.write(f"*Source:* {entry['source']}  \n")
            if entry.get('published'):
                f.write(f"*Published:* {entry['published']}  \n")
            f.write(f"*Category:* {entry['category']}\n\n")
            f.write(f"{entry['summary']}\n")
            f.write("\n---\n\n")
    
    print(f"✅ Digest saved to: {output_path}")

def main():
    print("🚀 Running Digest Agent...")
    digest_entries = run_digest_pipeline()
    print(f"✅ Processed {len(digest_entries)} articles.")
    
    save_digest_to_markdown(digest_entries)

if __name__ == "__main__":
    main()