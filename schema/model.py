from pydantic import BaseModel
class TranslationRequest(BaseModel):
    source_lang: str
    source_code: str
    target_lang: str
    target_code: str
    text: str


class TranslationRequest_facebook(BaseModel):
    text: str
    # src_lang: str
    # tgt_lang: str