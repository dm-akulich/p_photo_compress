# from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw
import os

print('*** Program Started ***')

# image_font_path = '/home/conquistador/code/github/python-01-utilities/image/fonts/'
image_path_input = '/Users/dima/Documents/dev/crawler-compressor/'
image_path_output = '/Users/dima/Documents/dev/crawler-compressor/'
# image_name_input = '05_compress_image_01_input.png'
image_name_input = 'img-input.jpg'

im = Image.open(image_path_input + image_name_input)
print('Input file size   : ', im.size )
print('Input file name   : ', image_name_input )
print('Input Image Size  : ', os.path.getsize (image_path_input  + image_name_input))

# image_name_output = '05_compress_image_01_output.png'
image_name_output = 'img_output.jpg'

im.save(image_path_output + image_name_output ,optimize=True,quality=50) 

print('Output file size  : ', im.size )
print('Output file name  : ', image_name_output)
print('Output Image Size : ', os.path.getsize (image_path_output + image_name_output))

print('*** Program Ended ***')
x = input('Нажмите enter чтобы закрыть', )
