import requests
from pprint import pprint
import random



def get_spacex_pictures():
    SpaceX_url = "https://api.spacexdata.com/v3/launches"
    response = requests.get(SpaceX_url)
    response.raise_for_status()
    # pictures_url = response.json()[72]["links"]["flickr_images"]
    a = response.json()
    # count = 0
    # for i in pictures_url:
    #     picture_response = requests.get(i)
    #     picture_response.raise_for_status()
    #     with open(f'SpaceX_pictures/SpaceX{count}.jpeg', "wb") as file:
    #         file.write(picture_response.content)
    #         count = count+1
    b = []
    for i in a:
        if not i["links"]["flickr_images"]==[]:
            b.append(i)
    links = random.choice(b)["links"]["flickr_images"]
    count = 0
    for i in links:
        picture_response = requests.get(i)
        picture_response.raise_for_status()
        with open(f'SpaceX_pictures/SpaceX{count}.jpeg', "wb") as file:
            file.write(picture_response.content)
            count = count+1