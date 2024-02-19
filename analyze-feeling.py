import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def analyze_sentiment(text):
    prompt = f"Analiza el sentimiento predominante en el siguiente texto: '{text}'. El sentimiento es: "
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=100,
        n=1
    )
    return response.choices[0].message.content.strip()

text = input("Ingresa un texto: ")
sentiment = analyze_sentiment(text)
print(sentiment)