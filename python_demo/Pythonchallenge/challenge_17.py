#!usr/bin/python
# -*- coding:utf-8 -*-

# http://www.pythonchallenge.com/pc/return/romance.html username : huge password : file
# you+should+have+followed+busynothing...
# %B2hs%C0%9Fy%E3D%BC%8B%EB%B8i%98lu2o%5D%C9%A0
from urllib import request, response, parse
import urllib
from http import cookies, cookiejar
import bz2

# postdata = urllib.parse.urlencode({
#     'Username': 'huge',
#     'Password': 'file'
# }).encode('utf-8')
#
# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     # "Accept-Encoding":"    gzip, deflate, br",
#     "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
#     "Authorization": "Basic aHVnZTpmaWxl",  # 授权头，账号密码
#     "Connection": "keep-alive",
#     "Host": "www.pythonchallenge.com",
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/55.0"
# }
# # url = r'http://www.pythonchallenge.com/pc/return/romance.html'
# url_linkedlist = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
# url_linkedlist1 = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345'
#
#
# def getcookie(req):
#     # 声明一个CookieJar对象实例来保存cookie
#     ck = cookiejar.CookieJar()
#     # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
#     handler = request.HTTPCookieProcessor(ck)
#     # 通过CookieHandler创建opener
#     opener = request.build_opener(handler, request.HTTPHandler)
#     r = opener.open(req)
#     htmltext = r.read().decode()
#     nothing = htmltext.split(' ')[-1]
#     print(htmltext + "-------" + nothing)
#
#     opener.close()
#     for item in ck:
#         # return (item.name + " : " + item.value)
#         return (item.value, nothing)
#
#
# nothing = '12345'
# list = []
# for i in range(400):
#
#     if nothing != 'it.':
#         req = request.Request(url_linkedlist + nothing, postdata, header)
#         reqcookie = getcookie(req)
#         print(i, end=" ： ")
#         nothing = reqcookie[1]
#         list.append(reqcookie[0])
#
# answer = "".join(list)
# print("------")
# print(answer)
# print(bz2.decompress(parse.unquote_to_bytes(answer.replace('+', '%20'))).decode('ascii'))
# from xmlrpc import client
#
# x = client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
# response = x.phone("Leopold")
# print(response)
from urllib import request
o = request.build_opener()
# message = "the flowers are on their way"
o.addheaders.append(('Cookie', 'info=the flowers are on their way'))
res = o.open("http://www.pythonchallenge.com/pc/stuff/violin.php")
print(res.read())
