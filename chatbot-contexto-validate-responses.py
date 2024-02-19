import openai
import os
import spacy
import numpy as np
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

previous_questions = []
previous_responses = []
modelo_spacy = spacy.load("es_core_news_md")
forbidden_words = ["Madrid", "madrid"]

def cosine_similarity(vec1, vec2):
    superposition = np.dot(vec1, vec2)
    magnitud1 = np.linalg.norm(vec1)
    magnitud2 = np.linalg.norm(vec2)
    cos_sim = superposition / magnitud1 * magnitud2
    return cos_sim

def is_it_relevant(response, entry, umbral=0.5):
    entry_vec = modelo_spacy(entry).vector
    response_vec = modelo_spacy(response).vector
    similarity = cosine_similarity(entry_vec, response_vec)
    print(similarity)
    return similarity >= umbral

def filter_black_list(text, black_list):
    tokens = modelo_spacy(text)
    result = []
    
    for token in tokens:
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
    print(response_gpt)
    relevant = is_it_relevant(response_gpt, input_user)
    if relevant:
        print(f"Chatbot: {response_gpt}")
        previous_questions.append(input_user)
        previous_responses.append(response_gpt)
    else: 
        print("La respuesta no es relevante")