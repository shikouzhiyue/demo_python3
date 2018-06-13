'''113.65.10.188	9797	HTTPS	透明	山东济南	xicidaili
记录2994:	27.46.74.61	9999	HTTPS	透明	山东济南	xicidaili
记录2698:	110.243.165.191	80'''
import urllib.request
import random

url = 'http://www.whatismyip.com.tw'
iplist = ['219.142.211.165:8118']

proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)