from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from src.llm_client import get_local_llm

# Reuse local LLM (Mistral through Ollama)
llm = get_local_llm()

def short_summary_chain():
    """Chain for summarizing short articles into 3 concise bullet points."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that summarizes articles concisely."),
        ("human", "Summarize the following article into exactly 3 bullet points:\n\n{content}")
    ])
    return prompt | llm
    # return LLMChain(llm=llm, prompt=prompt)

def detailed_summary_chain():
    """Chain for summarizing detailed articles into 5 bullet points + 3 insights."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a world-class expert at deep summarization."),
        ("human", "Summarize the following article into:\n\n- 5 key bullet points\n- 3 deep insights\n\nArticle:\n\n{content}")
    ])
    return prompt | llm
    # return LLMChain(llm=llm, prompt=prompt)