
from PIL import Image

left = int(input("Pixels from left : "))
upper = int(input("Pixels from upper : "))
right = int(input("Pixels from right : "))
lower = int(input("Pixels from lower : "))
img_path = str(input("Enter image path : "))

open_img = Image.open(img_path)
crop_image = open_img.crop((left, upper, right, lower))
crop_image.show()
