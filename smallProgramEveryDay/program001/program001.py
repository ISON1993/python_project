from PIL import Image,ImageDraw,ImageFont

def add_num(file,num,font_name,color):
    xsize,ysize = file.size
    draw = ImageDraw.Draw(file)
    text = str(num)
    font = ImageFont.truetype(font_name,xsize//3)
    draw.text((0,0), text, color, font)
    file.show()

image = Image.open("in.jpg")
num = 4
color = (0,0,0)
font_name = "verdana.ttf"
add_num(image,num,font_name,color)
