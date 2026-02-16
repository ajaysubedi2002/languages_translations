from pydantic import BaseModel
from typing import Optional
class TranslationRequest(BaseModel):
    source_lang: str = "English"
    source_code: str = "en"
    target_lang: str = "Nepali"
    target_code: str = "ne"
    text: Optional[str] = None

class TranslationRequest_facebook(BaseModel):
    text: str
    src_lang: str
    tgt_lang: str
    
    
