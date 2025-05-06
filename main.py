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
      try:
        description = get_spacex_pictures()
      except:
         print("Error by geting SpaceX pictures")
         continue
      
      picture_paths = [f"SpaceX_pictures/{file_name}" for file_name in os.listdir("SpaceX_pictures")]
      
      try:
        send_pictures(tg_token, tg_chat_id, picture_paths, description)
      except:
         print("Error by sending SpaceX pictures to Telegram")
         continue
    
         
  else:
      try:
        get_nasa_pictures(token_nasa)
      except:
        print("Error by geting Nasa pictures")
        continue
      
      picture_paths = [f"Nasa_pictures/{file_name}" for file_name in os.listdir("Nasa_pictures")]

      try:
        send_pictures(tg_token, tg_chat_id, picture_paths, "Pictures of the day from Nasa")
      except:
        print("Error by sending Nasa pictures to Telegram")
        continue
  
  sleep(60)