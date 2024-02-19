import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def translation_text(text, language):
    prompt = f"Por favor, traduce el texto '{text}' al idioma '{language}'"
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

text = input("Escribe el texto que quieres traducir: ")
language = input("¿A que idioma lo quieres traducir?: ")
translated_text = translation_text(text, language)
print(translated_text)