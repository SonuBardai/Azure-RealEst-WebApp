import os

for i, image in enumerate(os.listdir()):
    new_name = f'{i}.jpg'
    os.rename(image, new_name)