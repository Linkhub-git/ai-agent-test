 
# lógica del reconocimiento de imágenes
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from utils import save_embeddings
from numpy import dot
from numpy.linalg import norm

model_path = 'C:/Users/andre/linkhub/01 - Linkhub/03 - Desarrollo/18 - AI Agent/ai-agent-front/models/mobilenet_v3_small_075_224_embedder.tflite'
BaseOptions = mp.tasks.BaseOptions
ImageEmbedder = mp.tasks.vision.ImageEmbedder
ImageEmbedderOptions = mp.tasks.vision.ImageEmbedderOptions
VisionRunningMode = mp.tasks.vision.RunningMode

def create_image_embedding(image):
    """
    Crea un embedding de una imagen utilizando el modelo especificado.

    Args:
        image (str): La ruta del archivo de imagen.

    Returns:
        Embedding: El embedding resultante de la imagen.
    """
    print("create_image_embedding START")
    options = ImageEmbedderOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    quantize=True,
    running_mode=VisionRunningMode.IMAGE)

    with ImageEmbedder.create_from_options(options) as embedder:
        # Load the input image from an image file.
        mp_image = mp.Image.create_from_file(image)
                
        # Perform image embedding on the provided single image.
        embedding_result = embedder.embed(mp_image)
        print(type(embedding_result.embeddings[0]))
        print("create_image_embedding END") 
        return embedding_result.embeddings[0]
    
def load_images_embeddings(images):
    """
    Carga y guarda los embeddings de una lista de imágenes.

    Args:
        images (list): Una lista de rutas de archivos de imagen.

    Returns:
        None
    """
    print("load_images_embeddings START")
    embeddings = []
    for image in images:
        embeddings.append(create_image_embedding(image))
    save_embeddings(embeddings)
    print("load_images_embeddings END")
    
   
def calculate_cosine_similarity(embedding_one, embedding_two):
    """
    Calcula la similitud coseno entre dos embeddings utilizando NumPy.

    Args:
        embedding_one (Embedding): El primer embedding.
        embedding_two (Embedding): El segundo embedding.

    Returns:
        float: La similitud coseno entre los dos embeddings.
    """
    print("calculate_cosine_similarity START")
    cos_sim = dot(embedding_one, embedding_two)/(norm(embedding_one)*norm(embedding_two))
    print(f"Similarity: {cos_sim}")
    print("calculate_cosine_similarity END")
    return cos_sim