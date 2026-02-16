from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from schema.model import TranslationRequest
from config import settings

def translate_gemma(request: TranslationRequest):
    
    system_prompt = f"""
You are a professional {request.source_lang} ({request.source_code}) to {request.target_lang} ({request.target_code}) translator.
Your goal is to accurately convey the meaning and nuances of the original {request.source_lang} text while adhering to {request.target_lang} grammar, vocabulary, and cultural sensitivities.
Produce only the {request.target_lang} translation, without any additional explanations or commentary.
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Please translate the following {request.source_lang} text into {request.target_lang}:\n\n{request.text}")
    ]
     
    llm = ChatOllama(model=settings.Translate_model, temperature=0.2, base_url=settings.OLLAMA_API_URL)


    response = llm.invoke(messages)

    return {
        "translation": response.content.strip()
    }
