import os
from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI

def get_local_llm():
    """Return the appropriate LLM based on environment."""
    env = os.getenv("RUN_ENV", "local")  # default is local

    if env == "local":
        return ChatOllama(model="mistral")
    elif env == "cloud":
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY not set for cloud environment")
        return ChatOpenAI(
            model="gpt-4o",
            temperature=0.5,
            openai_api_key=openai_api_key
        )
    else:
        raise ValueError("Unknown RUN_ENV setting")