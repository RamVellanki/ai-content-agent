from config_loader import load_topics
from feed_discoverer import get_latest_articles
from content_fetcher import fetch_article_content, fetch_youtube_transcript
from summarizer import summarize_text
from report_generator import generate_report

def is_youtube(url):
    return "youtube.com" in url or "youtu.be" in url

def main():
    topics = load_topics()
    print(f"Loaded Topics: {topics}")

    articles = get_latest_articles()
    print(f"Fetched {len(articles)} articles.")

    summaries = []
    for article in articles:
        url = article['link']
        if is_youtube(url):
            content = fetch_youtube_transcript(url)
        else:
            content = fetch_article_content(url)

        if content:
            summary = summarize_text(content)
            summaries.append({
                "title": article['title'],
                "link": article['link'],
                "topic": article['topic'],
                "summary": summary
            })

    generate_report(summaries)

if __name__ == "__main__":
    main()