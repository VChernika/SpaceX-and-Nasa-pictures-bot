import requests
from pprint import pprint


def get_nasa_pictures():
    Token_nasa = "SBTtwSVXBuNsdJjz9xx0Bh4mYJagRUQSXTvBTxI5"
    Nasa_url = "https://api.nasa.gov/planetary/apod"
    params_Nasa = {
        "api_key": Token_nasa,
        "count": 10,
    }
    response = requests.get(Nasa_url, params=params_Nasa)
    response.raise_for_status()
    count = 0
    for i in response.json():
        picture_response = requests.get(i["url"])
        picture_response.raise_for_status()
        with open(f'Nasa_pictures/picture{count}.jpeg', "wb") as file:
            file.write(picture_response.content)
            count = count+1