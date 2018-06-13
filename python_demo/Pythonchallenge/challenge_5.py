#!usr/bin/python
# -*- coding:utf-8 -*-
import requests
import pickle

hea = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

html = requests.get('http://www.pythonchallenge.com/pc/def/banner.p', headers=hea)

html.encoding = 'utf-8'
##print(html.text)

a = open('5.p', 'w')
a.write(html.text)
a.close()

b = open('5.p', 'r')
data = pickle.load(b)
b.close