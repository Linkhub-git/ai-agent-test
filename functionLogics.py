 
# lógica de las tools
import requests
from requests.auth import HTTPBasicAuth
import json

CONTENT_TYPE_JSON = 'application/json'

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def verify_identity(mly_email):
    print("verify_identity INIT")
    print("verify_identity mail")
    print(mly_email)
    url = "https://ai-agent-api-102818124359.europe-southwest1.run.app/verify_identity"
    headers = {
        'Content-Type': CONTENT_TYPE_JSON,
        'API_KEY': 'B0C4ShAmfnw1x9qM'
    }
    data = {
        'userMail': mly_email
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), auth=HTTPBasicAuth("ai-agent@mango.com", "S8j60ou679gAikBeiu67340DHHpWE7Gf"))
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        api_response = response.json()
        print(api_response)
        tool_response = api_response.get('userId')
        print(tool_response)
        return tool_response
    except Exception as e:
        print("Error al obtener el id de Usuario", e)
        return None

def greetings(prompt):
    try:
        return prompt
    except Exception as e:
        print("Error al obtener el prompt de ask clarification", e)
        return None

def ask_clarification(prompt):
    try:
        return prompt
    except Exception as e:
        print("Error al obtener el prompt de ask clarification", e)
        return None
    
def get_orders(mly_user_id):
    print("get_orders INIT")
    print("get_orders mly_user_id")
    print(mly_user_id)
    url = "https://ai-agent-api-102818124359.europe-southwest1.run.app/get_orders"
    headers = {
        'Content-Type': CONTENT_TYPE_JSON,
        'API_KEY': 'B0C4ShAmfnw1x9qM'
    }
    data = {
        'userId': mly_user_id
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), auth=HTTPBasicAuth("ai-agent@mango.com", "S8j60ou679gAikBeiu67340DHHpWE7Gf"))
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        api_response = response.json()
        print(api_response)
        tool_response = api_response.get('orders')
        print(tool_response)
        return tool_response
    except Exception as e:
        print("Error al obtener los pedidos del usuario", e)
        return None
    
def get_order_by_id(order_id):
    print("get_order_by_id INIT")
    print("get_order_by_id order_id")
    print(order_id)
    url = "https://ai-agent-api-102818124359.europe-southwest1.run.app/get_order_by_id"
    headers = {
        'Content-Type': CONTENT_TYPE_JSON,
        'API_KEY': 'B0C4ShAmfnw1x9qM'
    }
    data = {
        'orderId': order_id
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), auth=HTTPBasicAuth("ai-agent@mango.com", "S8j60ou679gAikBeiu67340DHHpWE7Gf"))
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        api_response = response.json()
        print(api_response)
        order = api_response.get('order')
        tool_response = []
        tool_response.append(order)
        print(tool_response)
        return tool_response
    except Exception as e:
        print("Error al obtener la iformacion del pedido del usuario", e)
        return None
    
def return_order(order_id, mly_user_id):
    print("return_order INIT")
    print("return_order order_id")
    print(order_id)
    print("return_order mly_user_id")
    print(mly_user_id)
    url = "https://ai-agent-api-102818124359.europe-southwest1.run.app/return_order"
    headers = {
        'Content-Type': CONTENT_TYPE_JSON,
        'API_KEY': 'B0C4ShAmfnw1x9qM'
    }
    data = {
        'userId': mly_user_id,
        'orderId': order_id
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), auth=HTTPBasicAuth("ai-agent@mango.com", "S8j60ou679gAikBeiu67340DHHpWE7Gf"))
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        api_response = response.json()
        print(api_response)
        if api_response.get('success') == True:
            tool_response = "api_response"
        else:
            tool_response = "No se ha podido devolver"
        print(tool_response)
        return tool_response
    except Exception as e:
        print("Error al cancelar el pedido del usuario", e)
        return None

def send_return_mail_confirmation(order_id):
    print("send_return_mail_confirmation INIT")
    print("send_return_mail_confirmation order_id")
    print(order_id)
    url = "https://ai-agent-api-102818124359.europe-southwest1.run.app/send_mail"
    headers = {
        'Content-Type': CONTENT_TYPE_JSON,
        'API_KEY': 'B0C4ShAmfnw1x9qM'
    }
    data = {
        'orderId': order_id
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), auth=HTTPBasicAuth("ai-agent@mango.com", "S8j60ou679gAikBeiu67340DHHpWE7Gf"))
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        api_response = response.json()
        print(api_response)
        return "Enviado"
    except Exception as e:
        print("Error al obtener la iformacion del pedido del usuario", e)
        return None
 
 
def get_stores_information():
    try:
        stores_information = read_text_file('prompts/Stores.txt')
        return stores_information
    except Exception as e:
        print("Error al obtener la inforamcion de las tiendas", e)
        return None
    
def get_mly_information(session_id):
    try:
        print("get_mly_information INIT")
        print("get_mly_information session_id")
        print(session_id)
        url = "https://ai-agent-api-102818124359.europe-southwest1.run.app/get_context"
        headers = {
            'Content-Type': CONTENT_TYPE_JSON,
            'API_KEY': 'B0C4ShAmfnw1x9qM'
        }
        data = {
            'sessionId': session_id
        }
        response = requests.post(url, headers=headers, data=json.dumps(data), auth=HTTPBasicAuth("ai-agent@mango.com", "S8j60ou679gAikBeiu67340DHHpWE7Gf"))
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        api_response = response.json()
        tool_response = "HOME PROVIDED CONTEXT:\n=========" + api_response.get('context') + "=========\nEND PROVIDED CONTEXT"
        print(tool_response)
        return tool_response

    except Exception as e:
        print("Error al obtener la inforamcion de Mango Likes You", e)
        return None

def get_routine(session_id):
    try:
        print("get_routine INIT")
        print("get_routine session_id")
        print(session_id)
        url = "https://ai-agent-api-102818124359.europe-southwest1.run.app/get_routine"
        headers = {
            'Content-Type': CONTENT_TYPE_JSON,
            'API_KEY': 'B0C4ShAmfnw1x9qM'
        }
        data = {
            'sessionId': session_id
        }
        response = requests.post(url, headers=headers, data=json.dumps(data), auth=HTTPBasicAuth("ai-agent@mango.com", "S8j60ou679gAikBeiu67340DHHpWE7Gf"))
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        api_response = response.json()
        tool_response = api_response.get('routine')
        print(tool_response)
        return tool_response

    except Exception as e:
        print("Error al obtener la rutina", e)
        return None

def get_memory(session_id):
    try:
        print("get_memory INIT")
        print("v session_id")
        print(session_id)
        url = "https://ai-agent-api-102818124359.europe-southwest1.run.app/get_memory"
        headers = {
            'Content-Type': CONTENT_TYPE_JSON,
            'API_KEY': 'B0C4ShAmfnw1x9qM'
        }
        data = {
            'sessionId': session_id
        }
        response = requests.post(url, headers=headers, data=json.dumps(data), auth=HTTPBasicAuth("ai-agent@mango.com", "S8j60ou679gAikBeiu67340DHHpWE7Gf"))
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        api_response = response.json()
        tool_response = api_response.get('memory')
        print(tool_response)
        return tool_response

    except Exception as e:
        print("Error al obtener la memoria", e)
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