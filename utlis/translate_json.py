from .translate_gemma import translate_text_llm
from schema.model import JSONTranslationRequest
def translate_json(data, req: JSONTranslationRequest):
    
    if isinstance(data, str):
        return translate_text_llm(data, req)
    if isinstance(data, dict):
        return {
            key: translate_json(value, req)  
            for key, value in data.items()
        }

    if isinstance(data, list):
        return [translate_json(item, req) for item in data]

    return data
