# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# model_name = "facebook/nllb-200-distilled-600M"

# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
# save_path = "models/nllb_model"
# tokenizer.save_pretrained(save_path)
# model.save_pretrained(save_path)

# print("Loaded from local folder successfully!: ", model_name)


# from transformers import MBartForConditionalGeneration, MBart50TokenizerFast


# model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
# tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

# save_path = "models/facebook_mbart"
# tokenizer.save_pretrained(save_path)
# model.save_pretrained(save_path)
# print("Loaded from local folder successfully!: ", "facebook/mbart-large-50-many-to-many-mmt")




