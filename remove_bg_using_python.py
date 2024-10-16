# pip install rembg Pillow

from rembg import remove
from PIL import Image


input_path = 'sample1.jpeg'
output_path = 'output1.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
