import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

modelo = "gpt-3.5-turbo"
prompt = "¿De que se trata la pelicula el Interestellar?"

response = openai.chat.completions.create(
    model=modelo,
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=1,
    max_tokens=100,
    n=3
)


for option in response.choices:
    print(option.message.content)
