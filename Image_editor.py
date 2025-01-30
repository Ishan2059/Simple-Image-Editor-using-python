from PIL import Image, ImageEnhance, ImageFilter
import os

path='./images'
pathout = '/editedImages'

for filename in os.listdir(path):
    image = Image.open(f"{path}/{filename}")
    edit = image.filter(ImageFilter.SHARPEN).convert('L')
    
    enhancer =  ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(1.5)
    
    clean_name = os.path.splitext(filename)[0]
    edit.save(f'.{pathout}/{clean_name}_edited.jpg')