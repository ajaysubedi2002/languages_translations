from langchain_ollama import ChatOllama
from config import settings

def get_llm():
    llm = ChatOllama(model=settings.Translate_model, base_url=settings.OLLAMA_API_URL, temperature=0)
    return llm