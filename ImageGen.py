import os, glob
from PIL import Image, ImageDraw

img = Image.new('1', (2, 2), "white")
myImg = []

for filename in glob.glob("*.png"):
    os.remove(filename)

for i in range (0,2):
    for j in range (0,2):
        for k in range (0,2):
            for l in range (0,2):
                myImg = [i*255,j*255,k*255,l*255]
                img.putdata(myImg)
                img.save('test'+str(i)+str(j)+str(k)+str(l)+'.png')
