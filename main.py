import os
import shutil
import random
from time import sleep

from SpaceX import get_spacex_pictures
from Nasa import get_nasa_pictures
from config import *
from tg_bot import *



def clear_folder(folder_path):
    shutil.rmtree(folder_path)
    os.mkdir(folder_path)

def make_folder_if_not_exists(folder_path):
  if not os.path.exists(folder_path):
      os.mkdir(folder_path)



make_folder_if_not_exists("Nasa_pictures")
make_folder_if_not_exists("SpaceX_pictures")

while True:
  clear_folder("SpaceX_pictures")
  clear_folder("Nasa_pictures")
  services = ["SpaceX", "Nasa"]
  random_sending = random.choice(services)
  if random_sending == "SpaceX":
      description = get_spacex_pictures()
      picture_paths = [f"SpaceX_pictures/{file_name}" for file_name in os.listdir("SpaceX_pictures")]
      send_pictures(tg_token, tg_chat_id, picture_paths, description)
  else:
      get_nasa_pictures(token_nasa)
      picture_paths = [f"Nasa_pictures/{file_name}" for file_name in os.listdir("Nasa_pictures")]
      send_pictures(tg_token, tg_chat_id, picture_paths, "Pictures of the day from Nasa")
  
  sleep(60)