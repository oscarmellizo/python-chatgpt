import openai
import os
import spacy
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

previous_questions = []
previous_responses = []
modelo_spacy = spacy.load("es_core_news_md")
forbidden_words = ["Madrid", "madrid"]

def filter_black_list(text, black_list):
    tokens = modelo_spacy(text)
    print("TOKENS ", tokens)
    result = []
    
    for token in tokens:
        print(token)
        if token.text not in black_list:
            result.append(token.text)
        else:
            result.append("[xxxx]")
            
    return " ".join(result)

def question_chat_gpt(prompt, modelo="gpt-3.5-turbo"):
    response = openai.chat.completions.create(
        model = modelo,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=150,
        n=1
    )
    result_whitout_control = response.choices[0].message.content.strip()
    result_filter = filter_black_list(result_whitout_control, forbidden_words)
    return result_filter

print("Bienvenido a nuestro chat basico. Escribe 'salir' cuando quieras terminar")

while True:
    
    input_user = input("\nTu:")
    if input_user == "salir":
        break
    
    historic_conversation = ""
    for question, response in zip(previous_questions, previous_responses):
        historic_conversation += f"El usuario pregunta: {question}\nChatGPT responde: {response}\n" 
    
    prompt = f"El usuario pregunta {input_user}"
    historic_conversation += prompt
    
    response_gpt = question_chat_gpt(historic_conversation)
    print(f"Chatbot: {response_gpt}")
    
    previous_questions.append(input_user)
    previous_responses.append(response_gpt)