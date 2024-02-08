import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = "gpt-3.5-turbo"
prompt = "Cuenta una historia breve sobre un viaje a un pais de Europa."

response = openai.chat.completions.create(
    model=modelo,
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=1,
    max_tokens=100,
    n=1
)

response = response.choices[0].message.content
print(response)

print("***")

modelo_spacy = spacy.load("es_core_news_md")
analysis = modelo_spacy(response)

ubication = None

for ent in analysis.ents:
    if ent.label_ == "LOC":
        ubication = ent
        break

if ubication:
    print(ubication)
    prompt2 = "Dime mas acerca de {ubication}"
    response2 = openai.chat.completions.create(
        model=modelo,
        messages=[
            {"role": "user", "content": prompt2}
        ],
        max_tokens=100,
        n=1
    )
    print(response2.choices[0].message.content)
