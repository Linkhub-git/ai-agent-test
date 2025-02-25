 
# lógica de las tools
import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']
 
def tool(prompt, model="gpt-3.5-turbo"):
    """
    Envía un prompt al modelo de OpenAI y devuelve la respuesta.
    """
    try:
       
        return "test"
    except Exception as e:
        print("Error al llamar a la API:", e)
        return None