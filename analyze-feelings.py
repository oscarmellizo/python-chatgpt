import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def analyze_sentiment(text):
    prompt = f"Por favor, analiza el sentimiento predominante en el siguiente texto: '{text}'. Y respondeme explicativamente"
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

with open("comments.txt") as f:
    coments = f.read()
sentiment = analyze_sentiment(coments)
print(sentiment)