 
# lógica de la creación de HTML
from utils import save_string_to_file, append_string_to_file

OUTPUT_DIR = "./output/"
OUTPUT_FORMAR = ".html"

def create_output_file(file_title):
    """
    Crea un archivo HTML de salida con una estructura básica.

    Args:
        file_title (str): El título del archivo HTML.

    Returns:
        None
    """
    print("create_output_file START")
    save_string_to_file("<!DOCTYPE html>\n<html lang=\"en\" xml:lang=\"en\">\n<head>\n<title>" + file_title + "</title>\n<style>\nh1 {text-align: center;}\nh2 {text-align: left;}\np {text-align: left;}\ndiv {text-align: center;}\nimg {display: block; margin-left: auto; margin-right: auto;}\nfigure {padding: 4px; margin: auto;}\nfigcaption {color: black; font-style: italic; padding: 2px; text-align: center;}\n</style>\n</head><body style=\"margin-top: 100px;margin-bottom: 100px;margin-right: 150px;margin-left: 80px;\">\n", OUTPUT_DIR + file_title + OUTPUT_FORMAR)
    print("create_output_file END")

def insert_title_1(file_title, title):
    """
    Inserta un título de nivel 1 en el archivo HTML.

    Args:
        file_title (str): El título del archivo HTML.
        title (str): El título de nivel 1 a insertar.

    Returns:
        None
    """
    print("insert_title_1 START")
    append_string_to_file("<h1 style=\"font-size:80px;font-family:arial, sans-serif;color:navy\"><b>" + title + "</b></h1>\n", OUTPUT_DIR + file_title + OUTPUT_FORMAR)  
    print("insert_title_1 END") 

def insert_title_2(file_title, title):
    """
    Inserta un título de nivel 2 en el archivo HTML.

    Args:
        file_title (str): El título del archivo HTML.
        title (str): El título de nivel 2 a insertar.

    Returns:
        None
    """
    print("insert_title_2 START")
    append_string_to_file("<h2 style=\"font-size:50px;font-family:arial, sans-serif;color:navy\"><b>" + title + "</b></h2>\n", OUTPUT_DIR + file_title + OUTPUT_FORMAR)
    print("insert_title_2 END")

def insert_text(file_title, text):
    """
    Inserta un párrafo de texto en el archivo HTML.

    Args:
        file_title (str): El título del archivo HTML.
        text (str): El texto a insertar.

    Returns:
        None
    """
    print("insert_text START")
    append_string_to_file("<p style=\"font-size:20px;font-family:arial, sans-serif\">" + text + "</p>\n", OUTPUT_DIR + file_title + OUTPUT_FORMAR)
    print("insert_text END")
    
def insert_image(file_title, image_title, image_caption):
    """
    Inserta una imagen con un pie de foto en el archivo HTML.

    Args:
        file_title (str): El título del archivo HTML.
        image_title (str): El nombre del archivo de la imagen.
        image_caption (str): El pie de foto de la imagen.

    Returns:
        None
    """
    print("insert_image START")
    append_string_to_file("<figure><img src=\"./pictures/" + image_title + "\" alt=\"" + image_title + "\" style=\"width:50%;\"/>\n<figcaption>" + image_caption + "</figcaption>\n</figure>\n", OUTPUT_DIR + file_title + OUTPUT_FORMAR)
    print("insert_image END")
    
def end_output_file(file_title):
    """
    Finaliza el archivo HTML cerrando las etiquetas HTML y body.

    Args:
        file_title (str): El título del archivo HTML.

    Returns:
        None
    """
    print("end_output_file START")
    append_string_to_file("</body>\n</html>", OUTPUT_DIR + file_title + OUTPUT_FORMAR)
    print("end_output_file END")