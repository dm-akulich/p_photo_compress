import os
from PIL import Image, ImageDraw

# path = r'/Users/dima/Documents/dev/crawler-compressor/images/'

# path_output = path[0:len(path)-1] + '-output' + '/'

list_of_images = []

def crawler(path):
    list_of_dirs_files = os.walk(path)
    for i in list_of_dirs_files:
        if i[2] != []:
            for image_name in i[2]:
                if image_name.endswith('.jpg') or image_name.endswith('.png'):
                    if i[0].endswith('/'):
                        list_of_images.append(i[0] + image_name)
                    else:
                        list_of_images.append(i[0] + '/' + image_name)


def compressor(list):
    set_of_images = list_of_images
    for img_path in set_of_images:
        image = Image.open(img_path)
        image.save(img_path ,optimize=True,quality=50)
    print('Готово')

# if __name__ == "__main__":
#     crawler(path)
#     compressor(list_of_images)
