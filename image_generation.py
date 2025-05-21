 
# lógica del reconocimiento de imágenes
import base64
from config import settings
from openai import OpenAI
client = OpenAI(
  api_key=settings.OPENAI_API_KEY
)

def concatenate_keys(array):
    """
    Concatena las URLs de los objetos en una lista.

    Args:
        array (list): Una lista de objetos que contienen una propiedad 'url'.

    Returns:
        str: Una cadena con las URLs concatenadas, cada una precedida por '- ' y separada por saltos de línea.
    """
    print("concatenate_keys START")
    if not isinstance(array, list):
        raise ValueError("El parámetro debe ser una lista de objetos")
    
    result = []
    for obj in array:
        print("pasa")
        print(type(obj))
        result.append("- " + obj.url)
    
    print("concatenate_keys END")
    return '\n'.join(result)

def save_base64_image(base64_string, output_file):
    """
    Guarda una imagen codificada en base64 en un archivo.

    Args:
        base64_string (str): La imagen codificada en base64.
        output_file (str): La ruta del archivo donde se guardará la imagen.

    Returns:
        None
    """
    print("save_base64_image START")
    # Decodificar la cadena base64
    image_data = base64.b64decode(base64_string)
    
    # Escribir los datos binarios en un archivo
    with open(output_file, 'wb') as file:
        file.write(image_data)
    print("save_base64_image END")

def save_images(array):
    """
    Guarda una lista de imágenes codificadas en base64 en archivos.

    Args:
        array (list): Una lista de objetos que contienen una propiedad 'b64_json' con la imagen codificada en base64.

    Returns:
        list: Una lista de nombres de archivos donde se guardaron las imágenes.
    """
    print("save_images START")
    if not isinstance(array, list):
        raise ValueError("El parámetro debe ser una lista de objetos")
    
    index = 0
    titles = []
    for obj in array:
        print("pasa")
        title = "output_" + str(index) + ".jpg"
        save_base64_image(obj.b64_json,"./output/pictures/" + title)
        titles.append(title)
        index += 1
    print("save_images END")
    return titles

def generate_image_by_url():
    """
    Genera imágenes a partir de una URL usando el modelo DALL-E 2.

    Returns:
        str: Una cadena con las URLs de las imágenes generadas.
    """
    print("generate_image_by_url START") 
    completion = client.images.generate(
                    model="dall-e-2",
                    prompt="A cute baby sea otter",
                    n=3,
                    size="512x512",
                    style="natural"
                )
    urls = concatenate_keys(completion.data)
    print("generate_image_by_url END")
    return urls

def generate_image_base64():
    """
    Genera imágenes codificadas en base64 usando el modelo DALL-E 2 y las guarda en archivos.

    Returns:
        list: Una lista de nombres de archivos donde se guardaron las imágenes.
    """
    print("generate_image_base64 START") 
    completion = client.images.generate(
                    model="dall-e-2",
                    prompt="A cute baby sea otter",
                    n=3,
                    size="512x512",
                    style="natural",
                    response_format="b64_json"
                )
    titles = save_images(completion.data)
    print("generate_image_base64 END")
    return titles