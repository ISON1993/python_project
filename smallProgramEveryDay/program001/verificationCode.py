from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def getRandomChar():
    return chr(random.randint(65, 90))
def getRandomColor():
    return (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255))
def getRandomColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 240
height = 60
im = Image.new('RGB',(width,height),(255,255,2545))
font = ImageFont.truetype("verdana.ttf",36)
draw = ImageDraw.Draw(im)
for x in range(width):
    for y in range(height):
        draw.point((x,y),getRandomColor())
for i in range(4):
    draw.text((60*i+10,10),getRandomChar(),fill=getRandomColor2(),font=font)

im = im.filter(ImageFilter.BLUR)
im.show()
