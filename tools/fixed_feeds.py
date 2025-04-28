import requests
import feedparser
from datetime import datetime

def get_rss_feed_articles(feed_url, source_name, limit=5):
    """Fetch articles from a given RSS feed URL."""
    try:
        feed = feedparser.parse(feed_url)
        articles = []
        for entry in feed.entries[:limit]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "source": source_name,
                "published": entry.published if hasattr(entry, 'published') else None
            })
        return articles
    except Exception as e:
        print(f"Error fetching RSS feed {feed_url}: {e}")
        return []

def get_all_fixed_feed_articles():
    """Combine articles from all fixed favorite sources."""
    articles = []

    # 1. Hacker News
    articles += get_rss_feed_articles(
        feed_url="https://news.ycombinator.com/rss",
        source_name="Hacker News"
    )

    # 2. Indie Hackers
    articles += get_rss_feed_articles(
        feed_url="https://www.indiehackers.com/rss.xml",
        source_name="Indie Hackers"
    )

    # 3
    # 3. Add more RSS sources here if needed (optional examples)
    articles += get_rss_feed_articles(
        feed_url="https://openai.com/blog/rss.xml",
        source_name="OpenAI Blog"
    )
    
    #4 
    # 4. Substack: Pragmatic Engineer
    articles += get_rss_feed_articles(
        feed_url="https://newsletter.pragmaticengineer.com/feed",
        source_name="Pragmatic Programmer"
    )

    # TODO: Add all rss feeds from config/topics.yaml and add them to the articles list
    return articles