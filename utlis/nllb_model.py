from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# from transformers import NllbTokenizer, M2M100ForConditionalGeneration
from config import settings
model_path = settings.model_path_nllb
class NLLBTranslator:
    def __init__(self, model_path):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

    def translate(self, text, src_lang, tgt_lang):
        self.tokenizer.src_lang = src_lang
        inputs = self.tokenizer(text, return_tensors="pt")

        target_token_id = self.tokenizer.convert_tokens_to_ids(tgt_lang)

        outputs = self.model.generate(
            **inputs,
            forced_bos_token_id=target_token_id,
            max_length=200
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


translator = NLLBTranslator(model_path)

# result = translator.translate(
#     text="hi everyone, how are you doing today? I hope you are all doing well.",
#     src_lang="eng_Latn",
#     tgt_lang="npi_Deva"
# )

# print(result)



