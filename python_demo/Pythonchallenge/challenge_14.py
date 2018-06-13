#!usr/bin/python
# -*- coding:utf-8 -*-
# import requests
# url = 'http://www.pythonchallenge.com/pc/return/wire.png'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
# picture = requests.get(url,headers=header)
# with open('wire.png','wb+') as f:
#     f.write(picture.content)
from PIL import Image

img = Image.open('wire.png')
result = Image.new(img.mode, (100, 100))
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# 方向为  ---->
#       .   |
#       |   .
#       <----
x, y = -1, 0
k = 0
steps = 200
while steps / 2 > 0:
    for vector in direction:
        step = steps // 2
        for i in range(step):
            x = x + vector[0]
            y = y + vector[1]
            pixel = img.getpixel((k, 0))
            result.putpixel((x, y), pixel)
            k += 1
        steps -= 1
result.show()
