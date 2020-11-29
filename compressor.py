# from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw
import os

print('*** Program Started ***')

image_path_input = '/Users/dima/Desktop/photo_compress_test/'
image_path_output = '/Users/dima/Desktop/photo_compress_test/'
image_name_input = 'pro16.png'

im = Image.open(image_path_input + image_name_input)
print('Input file size   : ', im.size)
print('Input file name   : ', image_name_input)
print('Input Image Size  : ', os.path.getsize(image_path_input + image_name_input))

# image_name_output = '05_compress_image_01_output.png'
image_name_output = 'pro16_comp.png'

im.save(image_path_output + image_name_output, optimize=True, quality=50)

print('Output file size  : ', im.size)
print('Output file name  : ', image_name_output)
print('Output Image Size : ', os.path.getsize(image_path_output + image_name_output))

print('*** Program Ended ***')
x = input('Нажмите enter чтобы закрыть', )
