#!usr/bin/python
# -*- coding:utf-8 -*-
'''118.249.39.226	9999	HTTPS	透明	山东济南	xicidaili
记录2999:	114.219.63.173	8118	HTTPS	高匿	山东济南	xicidaili
记录2994:	27.46.74.61	9999	HTTPS	透明	山东济南	xicidaili
记录2991:	183.153.38.235	808	HTTPS	高匿	山东济南	xicidaili
记录2990:	180.152.235.17	9797	HTTPS	透明	山东济南	xicidaili
记录1995:	112.85.106.49	9131	HTTPS	透明	山西太原	xicidaili
记录2692:	218.19.246.225	9000	HTTPS	透明	江苏	xicidaili
记录2700:	101.17.60.156	80	HTTPS	高匿	江苏	xicidaili	'''
import urllib.request as request
import random

url = 'www.baidu.com'
iplist = ['122.114.31.177:808']

'''proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Test_Proxy_Python3.5_maminyao')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
url = 'http://www.csdn.net/'''

#代理IP列表
#iplist = ['110.73.1.179:8123']
#创建ProxyHandler
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36
proxy_support = request.ProxyHandler({'http':random.choice(iplist)})
#创建Opener
opener = request.build_opener(proxy_support)
#添加 User Angent
opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)')]
#安装OPener
request.install_opener(opener)
#使用自己安装好的Opener
response = request.urlopen(url)
html = response.read().decode('utf-8')
print(html)