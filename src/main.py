from pathlib import Path
from PIL import Image
import ctypes
import random


images_to_choose_from = []

def createNewFolder ():
    currentDir = str(Path.cwd())
    newFolder = Path(currentDir + '/Wallpapers')

    newFolder.mkdir(parents=True, exist_ok=True)

    return newFolder


# Fetch images from the folder
def search_and_populate_images():
    newFolder = createNewFolder()
    for child in newFolder.iterdir(): 
        is_file = child.is_file()
        is_img = False

        if is_file:
            try:
                with Image.open(child) as img:
                    img.verify()

                    is_img = True
            except:
                pass
        
        if is_img: images_to_choose_from.append(child)

search_and_populate_images()

def set_desktop_background():
    if len(images_to_choose_from) > 0:
        randomIndex = random.randint(0, len(images_to_choose_from) - 1)

        image_chosen = str(images_to_choose_from[randomIndex])

        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_chosen, 0)

set_desktop_background()

