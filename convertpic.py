# -*- coding: utf-8 -*-
from PIL import Image

grey2char = ['@', '#', '$', '%', '&', '?', '*', 'o', '/', '{', '[', '(', '|', '!', '^', '~', '-', '_', ':', ';', ',',
             '.', '`', ' ']
count = len(grey2char)


def toText(image_file):
    image_file = image_file.convert('L')  # 转灰度
    result = ''  # 储存字符串
    for h in range(0, image_file.size[1]):  # height
        for w in range(0, image_file.size[0]):  # width
            gray = image_file.getpixel((w, h))
            result += grey2char[int(gray / (255 / (count - 1)))]
        result += '\r\n'
    return result


image_file = Image.open("nianko.jpg")  # 打开图片
image_file = image_file.resize((int(image_file.size[0]* 0.2), int(image_file.size[1] * 0.1)))  # 调整图片大小

output = open('output.txt', 'w')
output.write(toText(image_file))
output.close()


