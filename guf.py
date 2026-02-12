from llama_cpp import Llama

llm = Llama(model_path="model-q2k.gguf")

prompt = "<2ne> Hello, how are you?"
response = llm(prompt=prompt, max_tokens=100)
print("only the responses", response)
print(response["choices"][0]["text"])


