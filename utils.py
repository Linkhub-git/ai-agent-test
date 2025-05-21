 
# lógica de las tools
import json

def ensure_object(param):
    if isinstance(param, str):
        try:
            return json.loads(param)
        except json.JSONDecodeError:
            raise ValueError("La cadena proporcionada no es un JSON válido")
    elif isinstance(param, dict):
        return param
    else:
        raise ValueError("El parámetro debe ser una cadena JSON o un diccionario")


def dict_to_string(obj):
    secure_obj = ensure_object(obj)
    result = []
    for key, value in secure_obj.items():
        result.append(f'- {key} = "{value}"')
    
    return "<br>".join(result)

def create_reasoning_message(message):
    if "tool_calls" in message and message["role"] == "assistant":
        reasoning_message_start = "<b>Llamada a la herramienta:</b> " + message["tool_calls"][0]["function"]["name"]
        reasoning_message_end = "<b>Argumentos:</b><br>" + dict_to_string(message["tool_calls"][0]["function"]["arguments"])
        reasoning_message = reasoning_message_start + "<br>" + reasoning_message_end
        return reasoning_message
    elif "tool_call_id" in message and message["role"] == "tool":
        reasoning_message = "<b>Respuesta de la herramienta:</b> " + message["content"]
        return reasoning_message

def save_string_to_file(string, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(string)
        
def append_string_to_file(string, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(string)

def save_embeddings(data):
    """Función dummy para guardar embeddings.
    Ajusta la implementación según tus necesidades reales."""
    print("Guardando embeddings:", data)

def save_images_array_from_file(image_list):
    """
    Función de ejemplo para guardar o procesar una lista de imágenes.
    Puedes ajustar la implementación según tus necesidades.
    """
    print("Guardando imágenes:", image_list)

def save_documents_array_from_file(document_list):
    """
    Función de ejemplo para guardar o procesar una lista de documentos.
    """
    print("Guardando documentos:", document_list)