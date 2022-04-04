from email.mime import base
import random 
from PIL import Image
from IPython.display import display 
import os


variations = 8
image_count = 10
layers = 6

def filename():
    name =""
    for i in range(layers):
        name = name + str(random.randint(1, variations))
    return name

files = []

for i in range(image_count):
    name = filename()
    if name not in files: 
        files.append(name)


for item in files:
    bg_image = Image.open(f"./bg/{item[0]}.png").convert("RGBA")
    base_image = Image.open(f"./base/{item[1]}.png").convert("RGBA")
    eyes_image = Image.open(f"./eyes/{item[2]}.png").convert("RGBA")
    mouth_image = Image.open(f"./mouth/{item[3]}.png").convert("RGBA")
    nose_image = Image.open(f"./nose/{item[4]}.png").convert("RGBA")
    accessory_image = Image.open(f"./accessory/{item[5]}.png").convert("RGBA")


    combine1 = Image.alpha_composite(bg_image, base_image)
    combine2 = Image.alpha_composite(combine1, eyes_image)
    combine3 = Image.alpha_composite(combine2, mouth_image)
    combine4 = Image.alpha_composite(combine3, nose_image)
    combine5 = Image.alpha_composite(combine4, accessory_image)

    rgb_im = combine5.convert("RGBA")
    file_name = item + ".png"
    rgb_im.save("./generated/" + file_name)

