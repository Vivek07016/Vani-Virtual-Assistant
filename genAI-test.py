import google.generativeai as genai

genai.configure(api_key="enter your API here")

models = genai.list_models()


for model in models:
    print(model.name, "|", model.supported_generation_methods) # List all models and their supported generation methods
