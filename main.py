from fastapi import FastAPI
from fastapi.responses import JSONResponse
from nllb_model import translator  
from large_50_mmt import translation_model

app = FastAPI()

@app.get("/")
def read_root():    
    return {"message": "Welcome to the Language Translation API!"}


@app.post("/translate_50_mmt")
def translate_text_50_mmt(text: str, src_lang: str, tgt_lang: str):
    """ Args:
    text (str): "enter the text you want to translate"        
    src_lang="en_XX",
    
    tgt_lang="ne_NP"
    
    """
    try:
        translation = translation_model.translate(
            text=text,
            src_lang=src_lang,
            tgt_lang=tgt_lang
        )

        return JSONResponse(
            status_code=200,
            content={
                "source_text": text,
                "source_language": src_lang,
                "target_language": tgt_lang,
                "translation": translation[0]
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

    

@app.post("/translate_nllb_model")
def translate_text_nllb_model(text: str, src_lang: str, tgt_lang: str) -> str:
    """ Args:
    text (str): "enter the text you want to translate"        
    src_lang="eng_Latn",
    tgt_lang="npi_Deva"
    """
    
    try:
        translation = translator.translate(text, src_lang, tgt_lang)
        # result = translator.translate(text=text, src_lang=src_lang,tgt_lang=tgt_lang)
        return JSONResponse(
            status_code=200,
            content={"translation": translation}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )