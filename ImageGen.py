import os, glob
from PIL import Image, ImageDraw

img = Image.new('1', (3, 3), "white")
myImg = []

for filename in glob.glob("*.png"):
    os.remove(filename)

for i in range (0,2):
    for j in range (0,2):
        for k in range (0,2):
            for l in range (0,2):
                for m in range (0,2):
                    for n in range (0,2):
                        for o in range (0,2):
                            for p in range (0,2):
                                for q in range (0,2):
                                    myImg = [i*255,j*255,k*255,l*255,m*255,n*255,o*255,p*255,q*255]
                                    img.putdata(myImg)
                                    img.save('test'+str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)+'.png')
