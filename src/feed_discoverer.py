FEEDS = {
    "AI": [
        "https://www.aisafetynews.com/rss",
        "https://openai.com/blog/rss.xml"
    ],
    "SaaS": [
        "https://www.saastr.com/feed/",
    ],
    "IndieHacking": [
        "https://www.indiehackers.com/rss.xml",
    ],
    "EngineeringLeadership": [
        "https://www.indiehackers.com/rss.xml",
        "https://news.ycombinator.com/rss"
    ]
}

import feedparser

def get_latest_articles():
    all_articles = []
    for topic, feeds in FEEDS.items():
        for feed in feeds:
            parsed = feedparser.parse(feed)
            for entry in parsed.entries[:3]:  # latest 3 per feed
                all_articles.append({
                    'title': entry.title,
                    'link': entry.link,
                    'published': entry.published,
                    'topic': topic
                })
    return all_articles