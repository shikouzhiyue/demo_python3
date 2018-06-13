#!usr/bin/python
# -*- coding:utf-8 -*-
import re, zipfile

p = re.compile(r"Next nothing is (\d+)")
prefix = "D:/py_demo/pythonchallenge_6/"
seed = '90052'
comments = []
z = zipfile.ZipFile("D:/py_demo\pythonchallenge_6/channel.zip", "r")
while True:
    fname = prefix + seed + ".txt"
    info = z.getinfo(seed + ".txt").comment.decode('utf-8')
    # print(info)
    comments.append(info)
    text = open(fname, 'r').read()
    print(text)
    lists = p.findall(text)


    if lists:
        seed = lists[0]
        print("   Next is", seed)
    else:
        break

print(''.join(comments))
