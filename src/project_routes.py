from fastapi.responses import JSONResponse
from fastapi import APIRouter
from schema.model import TranslationRequest, TranslationRequest_facebook
from utlis.nllb_model import translator  
from utlis.large_50_mmt import translation_model
from utlis.translate_gemma import translate_gemma

app = APIRouter()

@app.get("/")
def read_root():    
    return {"message": "Welcome to the Language Translation API!"}

# @app.post("/translate_50_mmt")
# def translate_text_50_mmt(text: str, src_lang: str, tgt_lang: str):
#     """ Args:
#     text (str): "enter the text you want to translate"        
#     src_lang="en_XX",
    
#     tgt_lang="ne_NP"
    
#     """
#     try:
#         translation = translation_model.translate(
#             text=text,
#             src_lang=src_lang,
#             tgt_lang=tgt_lang
#         )

#         return JSONResponse(
#             status_code=200,
#             content={
#                 "source_text": text,
#                 "source_language": src_lang,
#                 "target_language": tgt_lang,
#                 "translation": translation[0]
#             }
#         )

#     except Exception as e:
#         return JSONResponse(
#             status_code=500,
#             content={"error": str(e)}
#         )


# article_hi = "my name is ajay"

# response = translation_model.translate(
#     text=article_hi,    
#     src_lang="en_XX",   
#     tgt_lang="ne_NP"
# )
 
# print("English -> Nepali:", response[0])


@app.post("/translate_50_mmt")
def translate_text_50_mmt(request: TranslationRequest_facebook):
    """ Args:
text (str): "enter the text you want to translate"        
src_lang="en_XX",
    
tgt_lang="ne_NP"
"""
    try:
        translation = translation_model.translate(
            text=request.text,
            src_lang="en_XX",
            tgt_lang="ne_NP"
            # src_lang=request.src_lang,
            # tgt_lang=request.tgt_lang
        )
        return {
            "source_text": request.text,
            "source_language": "en_XX",
            "target_language": "ne_NP",
            "translation": translation[0]
        }
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/translate_nllb_model")
def translate_text_nllb_model(text: str, src_lang: str, tgt_lang: str) -> str:
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