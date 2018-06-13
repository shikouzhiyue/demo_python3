# usr/bin/python
# -*- coding:utf-8 -*-
from PIL import Image
'''
不愧是别人的代码，自己想明白都要很长的时间，而且十分简单
'''
img = Image.open('mozart.gif')
for y in range(img.size[1]):
    # 获得像素点
    line = [img.getpixel((x, y)) for x in range(img.size[0])]
    #195 对应的是红色的灰度值
    idx = line.index(195)   #index查找到的第一个元素对应的位置
    #将一行的像素点重新排列，把红色出现的位置放在每一行开始的地方
    line = line[idx:] + line[:idx]
    # 重新排列像素点
    [img.putpixel((x, y), line[x]) for x in range(len(line))]

img.show()
