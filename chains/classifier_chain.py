from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from src.llm_client import get_local_llm

# Reuse local LLM (Mistral through Ollama)
llm = get_local_llm()

def classifier_chain():
    """Chain to classify an article into News, Guide, or Opinion."""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert at classifying articles."),
        ("human", """Classify the following article into one of the following categories:
        
        - News
        - Guide
        - Opinion
        
Only respond with the category name (News, Guide, or Opinion), nothing else.

Article:
{content}
""")
    ])
    return prompt | llm
    # return LLMChain(llm=llm, prompt=prompt)