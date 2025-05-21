 
# lógica del reconocimiento de imágenes
from config import settings
from openai import OpenAI
client = OpenAI(
  api_key=settings.OPENAI_API_KEY
)

def recognize_image_by_url(url):
    print("recognize_image_by_url START")
    """
    Reconoce el contenido de una imagen a partir de una URL.

    Args:
        url (str): La URL de la imagen.

    Returns:
        str: La descripción del contenido de la imagen.
    """
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": url,
                },
            },
        ],
    }],
)
    print("recognize_image_by_url END")
    return completion.choices[0].message.content

def recognize_image_b64(base64_image, prompt):
    """
    Reconoce el contenido de una imagen a partir de una cadena base64.

    Args:
        base64_image (str): La imagen codificada en base64.

    Returns:
        str: La descripción del contenido de la imagen.
    """
    print("recognize_image_b64 START")
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                },
            },
        ],
    }],
)
    print("recognize_image_b64 END")
    return completion.choices[0].message.content