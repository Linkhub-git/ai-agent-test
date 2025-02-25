import json
import os
from openai import OpenAI
client = OpenAI(
  api_key='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'
)
from functionsDefinitions import TOOLS
from functionLogics import get_weather, verify_identity, ask_clarification, get_orders, get_order_by_id, return_order, get_stores_information, get_mly_information, case_resolution
 
# Configurar la API Key
 
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def call_function(name, args):
    if name == "verify_identity":
        return verify_identity(**args)
    if name == "ask_clarification":
        return ask_clarification(**args)
    if name == "get_orders":
        return get_orders(**args)
    if name == "get_order_by_id":
        return get_order_by_id(**args)
    if name == "return_order":
        return return_order(**args)
    if name == "get_stores_information":
        return get_stores_information(**args)
    if name == "get_mly_information":
        return get_mly_information(**args)
    if name == "case_resolution":
        return case_resolution(**args)
    
def save_array_to_file(array, file_path):
    """
    Guarda un array de objetos en un archivo de texto.
    """
    json_string = json.dumps(array, indent=4)
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
        return array_de_objetos

def ask_ai_agent(query, model="gpt-3.5-turbo"):
    """
    Envía un prompt al modelo de OpenAI y devuelve la respuesta.
    """
    prompt = read_text_file('prompts/planning.txt')

    try:
        print("ask_ai_agent completion 1")
        memory_messages = read_array_from_file("memory/messages.txt")
        if len(memory_messages) > 0:
            messages = memory_messages
        else:
            messages = [
                    {"role": "system", "content": prompt}
                ]
        messages.append({"role": "user", "content": query})
        condicion = True
        while condicion:
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.7,
                max_tokens=200,
                tools=TOOLS
                
            )

            if completion.choices[0].message.content:
                messages.append({"role": "assistant", "content":completion.choices[0].message.content})  # append model's function call message
            if completion.choices[0].message.tool_calls and len(completion.choices[0].message.tool_calls) > 0:
                for tool_call in completion.choices[0].message.tool_calls:
                    name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)

                    result = call_function(name, args)
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result

                })
                continue
            
            condicion = False
            save_array_to_file(messages, 'memory/messages.txt')
            print("ask_ai_agent completion END")
            return completion.choices[0].message.content    
 
    except Exception as e:
        print("Error al llamar a la API:", e)
        return None