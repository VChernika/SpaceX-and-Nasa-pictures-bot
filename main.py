from SpaceX import get_spacex_pictures
from Nasa import get_nasa_pictures
import os
import shutil

def clear_folder(folder_path):
    shutil.rmtree(folder_path)
    os.mkdir(folder_path)

clear_folder("SpaceX_pictures")
clear_folder("Nasa_pictures")
get_spacex_pictures()
get_nasa_pictures()

