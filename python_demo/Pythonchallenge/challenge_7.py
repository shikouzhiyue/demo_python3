#!usr/bin/python
# -*- coding:utf-8 -*-
import requests
import re
from PIL import Image

# url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
# img_url = re.findall(r'src="(.*?)"', requests.get(url, headers=headers).text)[0]
# img = requests.get(url[:-len(url.split('/')[-1])] + img_url, headers=headers)
# with open(img_url, 'wb+') as f:
#     f.write(img.content)
picture = Image.open('oxygen.png')
# print(picture.size)
# for i in range(1,picture.size[1]):
#     print(picture.getpixel((10, i)),i)
# 阴影部分高度8个像素
# for i in range(1,picture.size[0]):
#     print(picture.getpixel((i, 45)),i)
# 阴影部分宽度607个像素
charlist = []
chlist = []
last_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
picture1 = picture.crop((0, 43, 607, 51)).convert('L')
for i in range(picture1.size[0]):
    charlist.append(picture1.getpixel((i, 5)))
# print(charlist)
# for i in charlist:
#     print(chr(i),end='')
# for i in range(len(charlist)):
#     if i == len(charlist) - 1:
#         break
#     else:
#         if charlist[i] != charlist[i + 1]:
#             chlist.append(charlist[i])
# print(chlist)
# for i in chlist:
#     print(chr(i), end='')
    # 得到想要的字符
for i in last_list:
    print(chr(i),end='')