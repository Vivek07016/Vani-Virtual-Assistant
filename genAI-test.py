import google.generativeai as genai

genai.configure(api_key="AIzaSyA07YOgtBKBvH9kaZaMhI6T34KbZHhOuuE")

models = genai.list_models()


for model in models:
    print(model.name, "|", model.supported_generation_methods) # List all models and their supported generation methods
