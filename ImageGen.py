import os, glob, math
from PIL import Image, ImageDraw

side = 2
max = 2**(side*side)

img = Image.new('1', (side, side), "white")
myImg = []

for filename in glob.glob("*.png"):
    os.remove(filename)

for i in range (0,max):
    format = "{:0"+str(int(math.ceil(math.log(max,2))))+"b}"
    bin = format.format(i)
    myImg = []
    for j in range (0,len(bin)):
        myImg.append(int(bin[j])*255)
        img.putdata(myImg)
        img.save('test'+bin+'.png')
