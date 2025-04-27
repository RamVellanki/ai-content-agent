from langchain.schema import SystemMessage, HumanMessage
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from llm_client import get_local_llm

llm = get_local_llm()

def short_summary_chain():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant summarizing short articles."),
        ("human", "Summarize briefly in 3 bullet points:\n\n{content}")
    ])
    return prompt | llm

def detailed_summary_chain():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a deep summarizer for detailed articles."),
        ("human", "Summarize the article in 5 bullet points and highlight 3 key insights:\n\n{content}")
    ])
    return prompt | llm

def classify_article_chain():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a classifier."),
        ("human", "Classify this article as either 'News', 'Opinion', or 'Guide'. Only respond with the category.\n\n{content}")
    ])
    return prompt | llm