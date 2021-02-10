import os
import sys
from PIL import Image


# Grab first and second CL argument
directory = sys.argv[1]
new_directory = sys.argv[2]


# Check if folder is new/exists, if not create it
if not os.path.isdir(new_directory):
    os.mkdir(new_directory)


# Loop through Pokedex and convert images to PNG
for file in os.listdir(directory):
    if file.endswith('.jpg'):
        img = Image.open(f'{directory}{file}')
        clean_name = os.path.splitext(file)[0]
        img.save(f'{new_directory}{clean_name}.png')
        print('Completed')