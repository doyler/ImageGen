import os, glob
from PIL import Image, ImageDraw

img = Image.new('1', (2, 2), "white")
myImg = []

for filename in glob.glob("*.png"):
    os.remove(filename)

for i in range (0,16):
    bin = "{:04b}".format(i)
    myImg = [int(bin[0])*255,int(bin[1])*255,int(bin[2])*255,int(bin[3])*255]
    img.putdata(myImg)
    img.save('test'+bin+'.png')
