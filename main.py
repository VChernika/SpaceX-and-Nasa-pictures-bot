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

while True:
  clear_folder("SpaceX_pictures")
  clear_folder("Nasa_pictures")
  services = ["SpaceX", "Nasa"]
  random_sending = random.choice(services)
  if random_sending == "SpaceX":
      description = get_spacex_pictures()
      send_pictures(tg_token, tg_chat_id, ["SpaceX_pictures/SpaceX1.jpeg","SpaceX_pictures/SpaceX0.jpeg"], description)
  else:
      get_nasa_pictures(token_nasa)
      send_pictures(tg_token, tg_chat_id, ["SpaceX_pictures/SpaceX1.jpeg","SpaceX_pictures/SpaceX0.jpeg"], "Picture of the day from Nasa")
  
  sleep(60)