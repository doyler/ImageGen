import os, glob, math, time
from PIL import Image, ImageDraw

side = 2
max = 2**(side*side)

img = Image.new('1', (side, side), "white")
myImg = []

for count in range (1,6):

    print "#\n#\n#Run #" + str(count)

    start = time.clock()

    for i in range (0,max):
        format = "{:0"+str(int(math.ceil(math.log(max,2))))+"b}"
        bin = format.format(i)
        myImg = []
        for j in range (0,len(bin)):
            myImg.append(int(bin[j])*255)
            img.putdata(myImg)
            img.save('test'+bin+'.png')

    end = time.clock()

    print "#\n#Generating " + str(side) + "x" + str(side) + " icons took " + str(end-start) + " seconds."
    print "#That is an average of " + str((end-start)/max) + " seconds per image."

    startDel = time.clock()

    for filename in glob.glob("*.png"):
        os.remove(filename)

    endDel = time.clock()

    print "#\n#Deleting " + str(side) + "x" + str(side) + " icons took " + str(endDel-startDel) + " seconds."




#Run #1
#
#Generating 2x2 icons took 0.107727725827 seconds.
#That is an average of 0.0067329828642 seconds per image.
#
#Deleting 2x2 icons took 0.0154085508282 seconds.
#
#
#Run #2
#
#Generating 2x2 icons took 0.124344575126 seconds.
#That is an average of 0.00777153594537 seconds per image.
#
#Deleting 2x2 icons took 0.0513641976664 seconds.
#
#
#Run #3
#
#Generating 2x2 icons took 0.106258355538 seconds.
#That is an average of 0.00664114722113 seconds per image.
#
#Deleting 2x2 icons took 0.0123401599304 seconds.
#
#
#Run #4
#
#Generating 2x2 icons took 0.116733109504 seconds.
#That is an average of 0.00729581934397 seconds per image.
#
#Deleting 2x2 icons took 0.0172877719911 seconds.
#
#
#Run #5
#
#Generating 2x2 icons took 0.17327694371 seconds.
#That is an average of 0.0108298089819 seconds per image.
#
#Deleting 2x2 icons took 0.0172201129446 seconds.
#
#
#Run #1
#
#Generating 3x3 icons took 5.27691324552 seconds.
#That is an average of 0.0103064711826 seconds per image.
#
#Deleting 3x3 icons took 0.319111944904 seconds.
#
#
#Run #2
#
#Generating 3x3 icons took 5.28957221771 seconds.
#That is an average of 0.0103311957377 seconds per image.
#
#Deleting 3x3 icons took 0.407860422575 seconds.
#
#
#Run #3
#
#Generating 3x3 icons took 5.22261278692 seconds.
#That is an average of 0.0102004155995 seconds per image.
#
#Deleting 3x3 icons took 0.325968179702 seconds.
#
#
#Run #4
#
#Generating 3x3 icons took 5.41868764121 seconds.
#That is an average of 0.0105833742992 seconds per image.
#
#Deleting 3x3 icons took 0.31416716673 seconds.
#
#
#Run #5
#
#Generating 3x3 icons took 5.455970964 seconds.
#That is an average of 0.0106561932891 seconds per image.
#
#Deleting 3x3 icons took 0.311049182813 seconds.
