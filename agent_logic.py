import json
import os
from openai import OpenAI
from config import settings
client = OpenAI(
  api_key=settings.OPENAI_API_KEY
)
from functionsDefinitions import TOOLS
from functionLogics import  greetings, save_memory
from openai.types.chat import ChatCompletionMessage
from utils import create_reasoning_message
from image_recognition import recognize_image_b64
from image_generation import generate_image_by_url
from image_generation import generate_image_base64
from image_processing import process_images, process_images_json
from image_embeddings import create_image_embedding, calculate_cosine_similarity, load_images_embeddings, calculate_cosine_similarity
from html_generation import create_output_file, insert_title_1, insert_title_2, insert_text, insert_image, end_output_file
import time
#from processing_json import process_card_jsons


def ensure_string(value):
    if isinstance(value, list):
        return json.dumps(value)
    elif isinstance(value, str):
        return value
    else:
        raise ValueError("El valor debe ser una lista o una cadena")
    
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"Contenido del archivo {file_path}:")
            print(content)
            return content
    except Exception as e:
        print(f"Error al leer el archivo {file_path}: {e}")
        raise
    
def call_function(name, session_id, args):
    if name == "greetings":
        return greetings(**args)
    
    
def chat_completion_message_to_dict(message):
    """
    Convierte un objeto ChatCompletionMessage a un diccionario.
    """
    return message.to_dict()

def dict_to_chat_completion_message(data):
    """
    Convierte un diccionario a un objeto ChatCompletionMessage.
    """
    return data.dict()

def save_array_to_file(array, file_path):
    """
    Guarda un array de objetos en un archivo de texto.
    """
    serializable_array = []
    for item in array:
        if isinstance(item, ChatCompletionMessage):
            serializable_array.append(chat_completion_message_to_dict(item))
        else:
            serializable_array.append(item)
    
    print("Guardamos memoria")
    json_string = json.dumps(serializable_array, ensure_ascii=False, indent=4)
    with open(file_path, 'w') as file:
        file.write(json_string)
    print(f"Array de objetos guardado en {file_path}")

def read_array_from_file(file_path):
    """
    Lee un archivo de texto y lo convierte a un array de objetos.
    """
    with open(file_path, 'r') as file:
        json_string = file.read()
        array_de_objetos = json.loads(json_string)
        deserialized_array = []
        for item in array_de_objetos:
            if hasattr(item, 'tool_calls') and len(item.tool_calls) > 0:
                deserialized_array.append(dict_to_chat_completion_message(item))
            else:
                deserialized_array.append(item)
        return deserialized_array
    
def read_routine(session_id):
    """
    Lee un archivo de texto y lo convierte a un array de objetos.
    """
    routine = get_routine(session_id)

    return routine
    
def read_memory(session_id):
    """
    Lee un archivo de texto y lo convierte a un array de objetos.
    """
    json_string = get_memory(session_id)
    array_de_objetos = json.loads(json_string)
    deserialized_array = []
    for item in array_de_objetos:
        if hasattr(item, 'tool_calls') and len(item.tool_calls) > 0:
            deserialized_array.append(dict_to_chat_completion_message(item))
        else:
            deserialized_array.append(item)
    return deserialized_array

def write_memory(array, session_id):
    """
    Guarda un array de objetos en un archivo de texto.
    """
    serializable_array = []
    for item in array:
        if isinstance(item, ChatCompletionMessage):
            serializable_array.append(chat_completion_message_to_dict(item))
        else:
            serializable_array.append(item)
    
    print("Guardamos memoria")
    json_string = json.dumps(serializable_array, indent=4)
    save_memory(session_id, json_string)
    print(f"Array de objetos guardado en memoria_{session_id}")

def ask_ai_agent(query, session_id, model="gpt-3.5-turbo"):
    """
    Envía un prompt al modelo de OpenAI y devuelve la respuesta.
    """
    try:
        print("ask_ai_agent completion START")
        #embedding_one = create_image_embedding('./output/pictures/output_0.jpg')
        #embedding_two = create_image_embedding('./output/pictures/output_0.jpg')
        #similarity = calculate_cosine_similarity(embedding_one, embedding_two)
        #embeddings = load_embeddings()
        #simirat = calculate_cosine_similarity_two(embeddings[0], embeddings[1])
        #images = read_images_array_from_file()
        #load_images_embeddings(images)
        #process_images()
        #cards_json = create_cards_jsons()
        #cards_json_string = json.dumps(cards_json, ensure_ascii=False)
        #with open('./data/cards_json_punto.json', 'w') as file:
        #    file.write(cards_json_string)
        process_card_jsons()
        
        memory_messages = read_array_from_file('./memory/messages.txt')
        
        if len(memory_messages) > 0:
            messages = memory_messages
        else:
            prompt = read_text_file('./prompts/planning.md')
            messages = [
                    {"role": "system", "content": prompt}
                ]
        messages.append({"role": "user", "content": query})
        condicion = True
        while condicion:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.2,
                tools=TOOLS
                
            )
            
            if completion.choices[0].message.tool_calls and len(completion.choices[0].message.tool_calls) > 0:
                # append model's function call message
                reasoning_message = create_reasoning_message(chat_completion_message_to_dict(completion.choices[0].message))
                messages.append(completion.choices[0].message)
                print(completion.choices[0].message)
                time.sleep(2)
                for tool_call in completion.choices[0].message.tool_calls:
                    name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)

                    result = call_function(name, session_id, args)
                    reasoning_message = reasoning_message + "<br>" + create_reasoning_message({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": ensure_string(result)
                })
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": ensure_string(result)

                })
                    time.sleep(2)
                yield {"razonamiento": reasoning_message, "respuesta": None}
                continue
            
            condicion = False
            messages.append({"role": "assistant", "content":completion.choices[0].message.content.replace('**', '*')}) 
            save_array_to_file(messages, './memory/messages.txt')
            print("ask_ai_agent completion END")
            yield {"razonamiento": "<b>Finalizado</b>", "respuesta": f"{completion.choices[0].message.content.replace('**', '*')}"}    
 
    except Exception as e:
        print("Error al llamar a la API:", e)
        return None