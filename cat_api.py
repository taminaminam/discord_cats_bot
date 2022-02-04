import requests

api_url = "https://thecatapi.com"


def get_url():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    response_json = response.json()[0]

    print(response_json)

    url = response_json["url"]
    print(url)
    return url
