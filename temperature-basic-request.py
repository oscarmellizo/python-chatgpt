import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = "gpt-3.5-turbo"
prompt = "Inventa un poema de 10 palabras sobre Python"

response = openai.chat.completions.create(
    model=modelo,
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=1
)

print(response.choices[0].message.content)