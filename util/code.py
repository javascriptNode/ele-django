from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random



def check_code(width=90, height=40, char_length=4, font_file='static/Aeron.ttf'):
    f = BytesIO()

    img = Image.new(
    	mode='RGB', 
    	size=(width, height),
        color=(
        	random.randint(200, 255), 
        	random.randint(200, 255), 
        	random.randint(200, 255),
        )
    )

    draw = ImageDraw.Draw(img, mode='RGB')

    char_list = []

    # 画字
    for i in range(char_length):
        char = random.choice([
        	chr(random.randint(65, 90)), 
        	str(random.randint(1, 9)), 
        	chr(random.randint(97, 122)), 
        ])
        font = ImageFont.truetype(font_file, random.randint(18, 30))
        draw.text(
        	[i * 20 + 5, 0], 
        	char, 
        	fill = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)), 
        	font = font
        )
        char_list.append(char)

    # 生成随机颜色
    def rndColor():  
        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=rndColor())

    img.show()
    img.save(f, "png")
    data = f.getvalue()
    s_code = ''.join(char_list)
    return data, s_code

# check_code()