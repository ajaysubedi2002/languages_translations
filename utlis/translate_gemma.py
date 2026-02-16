from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from schema.model import TranslationRequest
from config import settings
from schema.model import JSONTranslationRequest

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

def translate_text_llm(text: str, req: JSONTranslationRequest) -> str:

    system_prompt = f"""
You are a professional {req.source_lang} ({req.source_code}) to {req.target_lang} ({req.target_code}) translator.
Your goal is to accurately convey the meaning and nuances of the original {req.source_lang} text while adhering to {req.target_lang} grammar, vocabulary, and cultural sensitivities.
Produce only the {req.target_lang} translation, without any additional explanations or commentary.Translate **every single part of the input text**, including:
- Single words
- Numbers
- Dates
- Symbols
- Short phrases
- Slang or colloquial expressions

Do NOT skip anything.
Do NOT summarize, omit, or interpret.
Do NOT add explanations, comments, or notes.
Return ONLY the translated text, preserving the original format and punctuation.
Translate literally and completely, even if a segment seems trivial or repetitive.
"""

    llm = ChatOllama(model=settings.Translate_model, temperature=0.2, base_url=settings.OLLAMA_API_URL)


    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=text)
    ]

    response = llm.invoke(messages)
    return response.content.strip()
