from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from src.project_routes import app as routes_app

def get_application() -> FastAPI:
    """Get the FastAPI app instance."""
    _app = FastAPI(
        description="Tras - Language Translation API",)     

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"], 
        allow_headers=["*"], 
    )

    _app.include_router(routes_app)

    return _app

app = get_application()




# from fastapi import FastAPI, File, UploadFile
# import base64
# import requests

# app = FastAPI()

# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "translategemma:latest"  # can also use translategemma:12b if pulled

# def encode_image_to_base64(img_bytes):
#     return base64.b64encode(img_bytes).decode()

# @app.post("/translate-image/")
# async def translate_image(
# #   "source_lang": "English",
# #   "source_code": "en",
# #   "target_lang": "Nepali",
# #   "target_code": "ne",
# #   "text": "string"      
#     source_lang: str = "English",
#     target_lang: str = "Nepali",
#     source_code: str = "en",
#     target_code: str = "ne",    
#     file: UploadFile = File(...)
# ):
#     # Read file bytes
#     img_bytes = await file.read()

#     # Encode image to base64
#     img_b64 = encode_image_to_base64(img_bytes)

#     # Build the prompt
#     prompt = (
#         f"You are a professional {source_lang} ({source_code}) to {target_lang} ({target_code}) translator. Your goal is to accurately convey the meaning and nuances of the original {source_lang} text while adhering to {target_lang} grammar, vocabulary, and cultural sensitivities."
#         f"Produce only the {target_lang} translation, without any additional explanations or commentary. Please translate the following {source_lang} text into {target_lang}:"
        
#     )

#     # Prepare payload for Ollama API
#     payload = {
#         "model": MODEL_NAME,
#         "prompt": prompt,
#         "images": [img_b64],
#         "stream": False
#     }

#     # Call locally running Ollama
#     response = requests.post(OLLAMA_URL, json=payload)
#     data = response.json()

#     # Return translation
#     return {"translation": data.get("response", "")}


# from fastapi import FastAPI, File, UploadFile
# import base64
# import requests

# app = FastAPI()

# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "translategemma:latest"

# def encode_image_to_base64(img_bytes):
#     return base64.b64encode(img_bytes).decode()

# @app.post("/translate-image/")
# async def translate_image(
#     source_lang: str = "English",
#     target_lang: str = "Nepali",
#     source_code: str = "en",
#     target_code: str = "ne",    
#     file: UploadFile = File(...)
# ):
#     # Read image bytes
#     img_bytes = await file.read()
#     img_b64 = encode_image_to_base64(img_bytes)

#     # Build translation prompt
#     prompt = (
#         f"You are a professional {source_lang} ({source_code}) to {target_lang} ({target_code}) translator. "
#         f"Translate the text in the uploaded image into {target_lang}. "
#         f"Produce only the {target_lang} translation, without extra explanations."
#     )

#     # Prepare payload for Ollama API
#     payload = {
#         "model": MODEL_NAME,
#         "prompt": prompt,
#         "images": [img_b64],
#         "stream": False
#     }

#     # Call Ollama API
#     response = requests.post(OLLAMA_URL, json=payload)
#     data = response.json()

#     # Return translation
#     return {"translation": data.get("response", "")}





