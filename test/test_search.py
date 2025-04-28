from tools.web_search_tool import search_web

results = search_web("latest news on AI agents")
for res in results:
    print(res['title'])
    print(res['link'])
    print(res['snippet'])
    print("------")