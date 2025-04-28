from tools.fixed_feeds import get_all_fixed_feed_articles

articles = get_all_fixed_feed_articles()
for article in articles:
    print(article['title'])
    print(article['link'])
    print(article['source'])
    print(article['published'])
    print("------")