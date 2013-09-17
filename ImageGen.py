import os, glob, math
from PIL import Image, ImageDraw

img = Image.new('1', (2, 2), "white")
myImg = []

for filename in glob.glob("*.png"):
    os.remove(filename)

for i in range (0,16):
    format = "{:0"+str(int(math.ceil(math.log(16,2))))+"b}"
    bin = format.format(i)
    myImg = []
    for j in range (0,len(bin)):
        myImg.append(int(bin[j])*255)
        img.putdata(myImg)
        img.save('test'+bin+'.png')
