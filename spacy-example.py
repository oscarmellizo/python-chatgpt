#pip install spacy
import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = "gpt-3.5-turbo"
prompt = "Cuenta una historia breve."

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

for token in analysis:
    print(token.text, token.pos_, token.dep_, token.text)

print("----------")

for ent in analysis.ents:
    print(ent.text, ent.label_)