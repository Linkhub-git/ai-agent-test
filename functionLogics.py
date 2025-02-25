 
# lógica de las tools
import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']
 
def verify_identity(mly_email):
    try:
        return "2132132132"
    except Exception as e:
        print("Error al obtener el id de Usuario", e)
        return None

def ask_clarification(prompt):
    try:
        return prompt
    except Exception as e:
        print("Error al obtener el prompt de ask clarification", e)
        return None
    
def get_orders(mly_user_id):
    try:
        return ["123","321","456"]
    except Exception as e:
        print("Error al obtener los pedidos del usuario", e)
        return None
    
def get_order_by_id(order_id):
    try:
        return [{"order_id":"123","datetime":"2025-01-15T12:34:11Z","status":"returnable"}]
    except Exception as e:
        print("Error al obtener la iformacion del pedido del usuario", e)
        return None
    
def return_order(order_id):
    try:
        return "Cancelado"
    except Exception as e:
        print("Error al cancelar el pedido del usuario", e)
        return None
    
def get_stores_information():
    try:
        return "Las tiendas de mango tienen un horario de lunes a viernes de 10:00 a 22:00 y sábados y domingos de 10:00 a 20:00"
    except Exception as e:
        print("Error al obtener la inforamcion de las tiendas", e)
        return None
    
def get_mly_information():
    try:
        return "Por cada euro que gastes en Mango obtendrás 10 Likes."
    except Exception as e:
        print("Error al obtener la inforamcion de Mango Likes You", e)
        return None
    
def case_resolution(mly_email, resolution_details):
    try:
        return resolution_details
    except Exception as e:
        print("Error al obtener la inforamcion de Mango Likes You", e)
        return None