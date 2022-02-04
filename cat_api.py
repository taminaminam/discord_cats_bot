import io
from PIL import Image
import requests

api_url = "https://thecatapi.com"


def get_url():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    response_json = response.json()[0]

    print(response_json)

    url = response_json["url"]
    print(url)
    return url


def get_image_as_bytes():
    image_url = get_url()
    image_response = requests.get(image_url)
    image_response_bytes = io.BytesIO(image_response.content)
    image = Image.open(image_response_bytes, mode='r')
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    return image_bytes.getvalue()