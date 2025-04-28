from config_loader import load_topics
from feed_discoverer import get_latest_articles
from tools.content_fetcher import fetch_article_content, fetch_youtube_transcript
from summarizer import short_summary_chain, detailed_summary_chain, classify_article_chain
from report_generator import generate_report

def is_youtube(url):
    return "youtube.com" in url or "youtu.be" in url

def main():
    topics = load_topics()
    print(f"Loaded Topics: {topics}")

    articles = get_latest_articles()
    print(f"Fetched {len(articles)} articles.")

    short_summary = short_summary_chain()
    detailed_summary = detailed_summary_chain()
    classifier = classify_article_chain()

    summaries = []

    for article in articles:
        url = article['link']
        if is_youtube(url):
            content = fetch_youtube_transcript(url)
        else:
            content = fetch_article_content(url)

        if not content:
            continue

        if len(content) < 500:
            summary = short_summary.invoke({"content": content})['text']
        else:
            summary = detailed_summary.invoke({"content": content})['text']

        category = classifier.invoke({"content": content})['text']

        summaries.append({
            "title": article['title'],
            "link": article['link'],
            "topic": article['topic'],
            "summary": summary,
            "category": category
        })

    generate_report(summaries)

if __name__ == "__main__":
    main()