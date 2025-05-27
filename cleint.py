from openai import OpenAI
import os

# It's best to set your key in environment variables for security
client = OpenAI(
    api_key=""
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is Data Science?"}
    ]
)

print(response.choices[0].message.content)
