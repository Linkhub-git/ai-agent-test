import os
import json
import base64
from image_recognition import recognize_image_b64

def read_image_as_base64(image_path):
    print("read_image_as_base64 START")
    """
    Lee una imagen desde una ruta de archivo y la convierte a una cadena base64.

    Args:
        image_path (str): La ruta del archivo de imagen.

    Returns:
        str: La imagen codificada en base64.
    """
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    print("read_image_as_base64 END")
    return encoded_string

def process_images():
    """
    Procesa todas las imágenes en un directorio, las convierte a base64 y las imprime.

    El directorio de imágenes está especificado en la variable `directory`.
    """
    print("process_images START")
    directory = 'C:/Users/andre/linkhub/01 - Linkhub/03 - Desarrollo/18 - AI Agent/ai-agent-front/images'
    with os.scandir(directory) as images:
        for image in images:
            if image.is_file():
                image_path = os.path.join(directory, image.name)
                base64_image = read_image_as_base64(image_path)
                print(f"Imagen en base64: {base64_image}")
                recognize_image_b64(base64_image)
    print("process_images END")  
            
def process_images_json():
    """
    Lee una lista de nombres de archivos de imagen desde un archivo JSON, 
    convierte cada imagen a base64 y las imprime.

    El archivo JSON debe estar en la ruta './images.json' y contener una lista de nombres de archivos de imagen.
    """
    print("process_images_json START")
    with open('./images.json', 'r') as file:
        json_string = file.read()
        images_array = json.loads(json_string)
        for image in images_array:
            base64_image = read_image_as_base64('./images/' + image['imageId'])
            print(f"Imagen en base64: {base64_image}")
    print("process_images_json END")
            
        