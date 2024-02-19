import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def text_classification(text):
    categories = [
        "arte",
        "ciencia",
        "deportes",
        "economia",
        "educacion",
        "entretenimiento",
        "medio ambiente",
        "politica",
        "salud",
        "tecnologia"
    ]
    prompt = f"Por favor clasifica el siguiente texto '{text}' en una de estas categorias {','.join(categories)}"
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=50,
        n=1
    )
    return response.choices[0].message.content.strip()

text_to_classificate = input("Ingrese texto: ")
category = text_classification(text_to_classificate)
print(category)