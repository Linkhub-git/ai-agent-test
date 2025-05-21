 
# lógica de las tools
import requests
from requests.auth import HTTPBasicAuth
import json
from html_generation import create_output_file, insert_title_1, insert_title_2, insert_text, insert_image, end_output_file

CONTENT_TYPE_JSON = 'application/json'

def get_photo_recommendations(family):
    print("get_photo_recommendations INIT")
    print(f"get_photo_recommendations family {family}")
    
    try:
        print(tool_response)
        return tool_response
    except Exception as e:
        print("Error al obtener el id de Usuario", e)
        return None

def create_instructions(instructions):
    print("create_instructions INIT")
    print("create_instructions family")
    print(family)
    
    try:
        print(tool_response)
        return tool_response
    except Exception as e:
        print("Error al obtener el id de Usuario", e)
        return None

def generate_images(features):
    print("create_instructions INIT")
    print("create_instructions family")
    print(family)
    
    try:
        print(tool_response)
        return tool_response
    except Exception as e:
        print("Error al obtener el id de Usuario", e)
        return None

def generate_html(title, text, images):
    print("generate_html INIT")
    print(f"generate_html title {title}")
    print(f"generate_html text {text}")
    print(f"generate_html images {images}")
    
    try:       
        create_output_file("output")
        insert_title_1(title)
        insert_title_2("Características recomendadas")
        insert_text(text)        
        insert_title_2("Imágenes de ejemplo")
        for image in images:
            insert_image(image, "Imagen de ejemplo1", "Imagen de ejemplo2")
        create_output_file("output")
        
    except Exception as e:
        print("Error al obtener el id de Usuario", e)
        return None

def greetings(prompt):
    try:
        return prompt
    except Exception as e:
        print("Error al obtener el prompt de ask clarification", e)
        return None
    
def save_memory(session_id, memory):
    try:
        print("get_memory INIT")
        print("v session_id")
        print(session_id)
        url = "https://ai-agent-api-102818124359.europe-southwest1.run.app/save_memory"
        headers = {
            'Content-Type': CONTENT_TYPE_JSON,
            'API_KEY': 'B0C4ShAmfnw1x9qM'
        }
        data = {
            'sessionId': session_id,
            'memory': memory
        }
        response = requests.post(url, headers=headers, data=json.dumps(data), auth=HTTPBasicAuth("ai-agent@mango.com", "S8j60ou679gAikBeiu67340DHHpWE7Gf"))
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        api_response = response.json()
        tool_response = api_response.get('success')
        print(tool_response)
        return "Memoria Guardada"

    except Exception as e:
        print("Error al guardar la memoria", e)
        return None
       
def case_resolution(mly_email, resolution_details):
    try:
        return resolution_details
    except Exception as e:
        print("Error al obtener la inforamcion de Mango Likes You", e)
        return None