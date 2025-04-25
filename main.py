from SpaceX import get_spacex_pictures
from Nasa import get_nasa_pictures
import os
import shutil
from config import *
import requests
import json
from pprint import pprint
import random
from time import sleep



def send_pictures(token, chat_id, file_picture_names, text):

  media = []
  for number, i in enumerate(file_picture_names, start=1):
        media.append({
            "type": "photo",
            "media": f"attach://random-name-{number}"
    })
  media[0]["caption"] = text
  pprint(media)

  params = {
      "chat_id": chat_id,
      "media": json.dumps(media),
      "contentType": "application/json"
  }

  files = {}


  for number, i in enumerate(file_picture_names, start=1):
    files[f"random-name-{number}"] = open(i, "rb")

  print(files)

  send_text = f'https://api.telegram.org/bot{token}/sendMediaGroup'
  response = requests.post(send_text, params=params, files=files)
  response.raise_for_status()
  print(response.text)


def clear_folder(folder_path):
    shutil.rmtree(folder_path)
    os.mkdir(folder_path)

while True:
  clear_folder("SpaceX_pictures")
  clear_folder("Nasa_pictures")
  a = ["SpaceX", "Nasa"]
  r = random.choice(a)
  if r == "SpaceX":
      d = get_spacex_pictures()
      send_pictures(tg_token, tg_chat_id, ["SpaceX_pictures/SpaceX1.jpeg","SpaceX_pictures/SpaceX0.jpeg"], d)
  else:
      get_nasa_pictures(token_nasa)
      send_pictures(tg_token, tg_chat_id, ["SpaceX_pictures/SpaceX1.jpeg","SpaceX_pictures/SpaceX0.jpeg"], "Picture of the day from Nasa")
  
  sleep(60)
  