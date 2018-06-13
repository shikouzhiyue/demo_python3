#!usr/bin/python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://www.xicidaili.com/nn/'
ip_list = []
proxies = {}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
html = requests.get(url, headers=headers)
Soup = BeautifulSoup(html.text, 'lxml').find('table', id='ip_list').find_all('tr', class_='odd')
count = 0
for i in Soup:
    count = count + 1
    ip = i.find_all('td')[1].get_text()
    ip_proxy = 'http://' + str(ip)
    proxies['https'] = ip_proxy
    try:
        requests.get('https://www.baidu.com', headers=headers, proxies=proxies, timeout=5)
        ip_list.append(ip)
    except Exception as e:
        print(e)
    if count == 20:
        break
print(ip_list)
