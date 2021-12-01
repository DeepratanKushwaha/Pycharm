
from PIL import Image

open_image = Image.open(r"C:/Users/mss2015/Desktop/wallpaper/5n.jpg")
convert_to_bw = open_image.convert("L")
convert_to_bw.show()

