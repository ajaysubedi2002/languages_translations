from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schema.model import JSONTranslationRequest, TranslationRequest
from utlis.nllb_model import translator  
from utlis.large_50_mmt import translation_model
from utlis.translate_gemma import translate_gemma
from fastapi import UploadFile, File
import requests
from utlis.encode_image import encode_image_to_base64
from config import settings
from utlis.translate_json import translate_json
from fastapi import UploadFile, File
import json

app = APIRouter()

@app.get("/")
def read_root():    
    return {"message": "Welcome to the Language Translation API!"}

@app.post("/translate_50_mmt")
def translate_text_50_mmt(text:str, src_lang:str="en_XX", tgt_lang:str="ne_NP"):
    """ Args:
text (str): "enter the text you want to translate",       
src_lang="en_XX",    
tgt_lang="ne_NP"
    """
    try:
        translation = translation_model.translate(
            text = text,
            src_lang = src_lang,
            tgt_lang = tgt_lang,
        
        )
        return {
            "source_text": text,
            "source_language": src_lang,
            "target_language": tgt_lang,
            "translation": translation[0]
        }
    except Exception as e:
        return {"error": str(e)}
   
     
@app.post("/translate_nllb_model")
def translate_text_nllb_model(text: str, src_lang: str = "eng_Latn", tgt_lang: str = "npi_Deva") -> str:
    """ Args:
    text (str): "enter the text you want to translate"        
    src_lang="eng_Latn",
    tgt_lang="npi_Deva"
    """
    
    try:
        translation = translator.translate(text, src_lang, tgt_lang)
        return JSONResponse(
            status_code=200,
            content={"translation": translation}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
        
        
@app.post("/translate_gemma")  
  
def translate_text_gemma(request: TranslationRequest):
    
    """ Args:
  text (str): "enter the text you want to translate"
  "source_lang": "English",
  "source_code": "en",
  "target_lang": "Nepali",
  "target_code": "ne",
  "text": "string"      

"""
    try:
        translation = translate_gemma(request)
        return JSONResponse(
            status_code=200,
            content={"translation": translation["translation"]}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

@app.post("/translate-image/")
async def translate_image(
    source_lang: str = "English",
    target_lang: str = "Nepali",
    source_code: str = "en",
    target_code: str = "ne",    
    file: UploadFile = File(...)
):
    OLLAMA_GENERATE_URL = f"{settings.OLLAMA_API_URL}/api/generate"
    img_bytes = await file.read()
    img_b64 = encode_image_to_base64(img_bytes)

    prompt = (
        f"You are a professional {source_lang} ({source_code}) to {target_lang} ({target_code}) translator. "
        f"Translate the text in the uploaded image into {target_lang}. "
        f"Produce only the {target_lang} translation, without extra explanations."
    )

    payload = {
        "model": settings.Translate_model,
        "prompt": prompt,
        "images": [img_b64],
        "stream": False
    }
    # Call Ollama API
    response = requests.post(OLLAMA_GENERATE_URL, json=payload)
    data = response.json()

    return {"translation": data.get("response", "")}
   



@app.post("/translate-json-file")
async def translate_json_file(
    source_lang: str = "Nepali",
    source_code: str = "ne",
    target_lang: str = "English",
    target_code: str = "en",
    file: UploadFile = File(...)
):
    raw_json = json.loads(await file.read())

    req = JSONTranslationRequest(
        source_lang=source_lang,
        source_code=source_code,
        target_lang=target_lang,
        target_code=target_code,
        data=raw_json
    )

    translated_data = translate_json(raw_json, req)
    return {"translated_data": translated_data}
