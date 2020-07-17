from PIL import Image
import os
import sys
os.chdir(sys.path[0])
img = Image.open("ascii.jpg")
out = img.convert("L")
out = out.resize((int (500),int (250)))
width,height = out.size
text = ""
asciis = "@%#*+=-. "
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col,row))
        text += asciis[int (gray/255*8)]
    text+=("\n")
file = open("ascii.txt","w")
file.write(text)
file.close
