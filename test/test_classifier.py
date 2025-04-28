from chains.classifier_chain import classifier_chain

chain = classifier_chain()
output = chain.invoke({"content": "This is an article discussing the recent updates to AI research and their impact on society."})
print(output['text'])