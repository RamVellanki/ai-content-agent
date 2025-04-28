from chains.summarizer_chain import short_summary_chain

chain = short_summary_chain()
output = chain.invoke({"content": "Your article text here..."})
print(output['text'])