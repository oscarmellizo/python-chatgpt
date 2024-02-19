import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def create_content(subject, tokens, temperature, model="gpt-3.5-turbo"):
    prompt = f"Por favor escribe un articulo corto sobre el tema: {subject}\n\n"
    response = openai.chat.completions.create(
        model = model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=tokens,
        n=1
    )
    return response.choices[0].message.content.strip()

def text_summary(text, tokens, temperature, model="gpt-3.5-turbo"):
    prompt = f"Por favor resume el siguiente texto: {text}\n\n"
    response = openai.chat.completions.create(
        model = model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=tokens,
        n=1
    )
    return response.choices[0].message.content.strip()

subject = input("Elije un tema para tu articulo: ")
tokens = int(input("Cuantos tokens maximos tendra tu articulo: "))
temperature = int(input("Del 1 al 10 que tan creativo quieres que sea tu articulo: ")) / 10

article_created = create_content(subject, tokens, temperature)
print(article_created)