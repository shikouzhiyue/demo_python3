# usr/bin/python
# -*- coding:utf-8-*-
from PIL import Image

im = Image.open('cave.jpg')
odd = Image.new(im.mode, (im.size[0] // 2, im.size[1] // 2))
even = Image.new(im.mode, (im.size[0] // 2, im.size[1] // 2))

for x in range(1, im.size[0] , 2):#取奇数行，列的像素
    for y in range(1, im.size[1], 2):
        odd.putpixel(((x - 1) // 2, (y - 1) // 2), im.getpixel((x, y)))

for x in range(0, im.size[0] , 2):#取偶数行列的像素
    for y in range(0, im.size[1], 2):
        even.putpixel((x // 2, y // 2), im.getpixel((x, y)))

odd.save('odd.jpg')
even.save('even.jpg')