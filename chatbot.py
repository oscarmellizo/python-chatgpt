import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def question_chat_gpt(prompt, modelo="gpt-3.5-turbo"):
    response = openai.chat.completions.create(
        model = modelo,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1.5,
        max_tokens=150,
        n=1
    )
    return response.choices[0].message.content

print("Bienvenido a nuestro chat basico. Escribe 'salir' cuando quieras terminar")

while True:
    input_user = input("\nTu:")
    if input_user == "salir":
        break
    
    prompt = f"El usuario pregunta {input_user}\nChatGPT responde:"
    response_gpt = question_chat_gpt(prompt)
    print(f"Chatbot: {response_gpt}")