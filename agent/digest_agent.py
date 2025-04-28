import random
from src.config_loader import load_topics
from tools.fixed_feeds import get_all_fixed_feed_articles
from tools.web_search_tool import search_web
from tools.content_fetcher import fetch_article_content
from chains.router_chain import choose_summarizer_chain
from chains.classifier_chain import classifier_chain

def discover_fixed_feeds():
    return get_all_fixed_feed_articles()

def discover_dynamic_search(topics, articles_per_topic=3):
    """Use web search tool to find latest articles dynamically."""
    all_articles = []
    for topic in topics:
        topic_name = topic['name']
        keywords = topic.get('keywords', [topic_name])

        query = random.choice(keywords) + " latest"  # Slight variation
        search_results = search_web(query, num_results=articles_per_topic)

        for item in search_results:
            all_articles.append({
                "title": item['title'],
                "link": item['link'],
                "source": "Web Search",
                "published": None
            })
    return all_articles

def fetch_and_process_article(article):
    """Fetch content, summarize, classify."""
    content = fetch_article_content(article['link'])

    if not content or len(content.strip()) == 0:
        return None

    summarizer = choose_summarizer_chain(content)
    summary_result = summarizer.invoke({"content": content})
    summary = summary_result.content

    classifier = classifier_chain()
    category_result = classifier.invoke({"content": content})
    category = category_result.content.strip()

    return {
        "title": article['title'],
        "link": article['link'],
        "source": article['source'],
        "published": article.get('published'),
        "summary": summary,
        "category": category
    }

def run_digest_pipeline():
    """Full pipeline to generate a digest."""

    topics = load_topics()

    print("Discovering fixed favorite articles...")
    fixed_articles = discover_fixed_feeds()

    print("Discovering dynamic fresh articles...")
    dynamic_articles = discover_dynamic_search(topics)

    all_articles = fixed_articles + dynamic_articles

    print(f"Total {len(all_articles)} articles found. Fetching content and summarizing...")

    digest_entries = []

    for article in all_articles:
        try:
            processed = fetch_and_process_article(article)
            if processed:
                digest_entries.append(processed)
        except Exception as e:
            print(f"Failed to process {article['link']}: {e}")

    return digest_entries