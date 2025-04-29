import requests
from pprint import pprint
import random



def get_spacex_pictures():
    spaceX_url = "https://api.spacexdata.com/v3/launches"
    response = requests.get(spaceX_url)
    response.raise_for_status()
    json_response = response.json()
    launches = []
    for i in json_response:
        if not i["links"]["flickr_images"]==[]:
            launches.append(i)
    launch = random.choice(json_response)
    links = launch["links"]["flickr_images"]
    description = launch["details"]
    count = 0
    for i in links:
        picture_response = requests.get(i)
        picture_response.raise_for_status()
        with open(f'SpaceX_pictures/SpaceX{count}.jpeg', "wb") as file:
            file.write(picture_response.content)
            count = count+1

    return description

