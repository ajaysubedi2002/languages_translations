from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import torch

model_path = "models/facebook_mbart"

class facebook_mbart:
    def __init__(self, model_path):
        self.model = MBartForConditionalGeneration.from_pretrained(model_path)
        self.tokenizer = MBart50TokenizerFast.from_pretrained(model_path)

    def translate(self, text, src_lang, tgt_lang):
        self.tokenizer.src_lang = src_lang
        encoded_text = self.tokenizer(text, return_tensors="pt")
       
        generated_tokens = self.model.generate(
            **encoded_text,
            forced_bos_token_id=self.tokenizer.lang_code_to_id[tgt_lang],
        )
        return self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    
    
translation_model = facebook_mbart(model_path)


# article_hi = "hellow how are you doing today? I hope you are all doing well."

# model = MBartForConditionalGeneration.from_pretrained(model_path)
# tokenizer = MBart50TokenizerFast.from_pretrained(model_path)

# # translate English to Nepali
# tokenizer.src_lang = "en_XX"
# encoded_hi = tokenizer(article_hi, return_tensors="pt")
# generated_tokens = model.generate(
#     **encoded_hi,
#     forced_bos_token_id=tokenizer.lang_code_to_id["ne_NP"]
# )
# ENG_to_NEPALI = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
# print("English -> Nepali:", ENG_to_NEPALI[0])