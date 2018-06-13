#!usr/bin/python
# -*- coding:utf-8 -*-
import requests
import re


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
# }
# url = 'https://www.kuaidaili.com/free/inha/1/'
# html = requests.get(url).text
# # print(html)
# ip_list = []
# pattern_ip = re.compile(r'"IP">(.*?)<')
# pattern_port = re.compile(r'"PORT">(.*?)<')
# ip = re.findall(pattern_ip, html)
# port = re.findall(pattern_port, html)
# for i, p in zip(ip, port):
#     ip_list.append(i.strip()+':'+p.strip())
#
# print(ip_list)

def a__(first, second, third=None):
    if third is None:
        return first + second
    else:
        return first+second+int(third)


print(a__(1, 2,3))
