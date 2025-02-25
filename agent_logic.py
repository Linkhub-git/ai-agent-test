import json
import os
from openai import OpenAI
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)
from functionsDefinitions import TOOLS
from functionLogics import get_weather
 
# Configurar la API Key
 
def ask_ai_agent(prompt, model="gpt-3.5-turbo"):
    """
    Envía un prompt al modelo de OpenAI y devuelve la respuesta.
    """
    
    
    try:
        print("ask_ai_agent completion 1")
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un AI Agent experto en ayudar a usuarios."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200,
            tools=TOOLS
            
        )
        
        tool_call = completion.choices[0].message.tool_calls[0]
        args = json.loads(tool_call.function.arguments)

        result = get_weather(args["latitude"], args["longitude"])

        messages = [{"role": "user", "content": prompt}]
        messages.append(completion.choices[0].message)  # append model's function call message
        messages.append({                               # append result message
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        })

        print("ask_ai_agent completion 2")
        completion_2 = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=200,
            tools=TOOLS
        )

        print("ask_ai_agent completion END")
        return completion_2.choices[0].message.content
    except Exception as e:
        print("Error al llamar a la API:", e)
        return None