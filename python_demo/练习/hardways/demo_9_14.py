#coding:utf-8
'''113.65.10.188	9797'''
import urllib.request
import re
page = 1
url = 'https://www.qiushibaike.com/hot/page/1/'+str(page)
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
headers = {'User-Agent':user_agent}

try:
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    qiubaiPattern =re.compile('<div.*?author.*?alt="(.*?)>.*?content.*?span>(.*?)</.*?number">(.*?)<',re.S)
    infos = re.findall(qiubaiPattern,response.read().decode('utf-8'))
    for info in infos:
        for a in info:
            str = a.replace('<br/>','\r\n') #将段子正文中的<br/>替换成回车
            print(str.strip()) #删除字符中的首尾空格

except urllib.request.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)