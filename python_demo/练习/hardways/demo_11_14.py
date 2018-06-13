import requests
from bs4 import BeautifulSoup
'''
使用reques库
增加header信息
但是图片下载失败。。。
'''
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    'Referer': 'http://blog.csdn.net/eric_sunah/article/details/11099295',
    'Host': 'blog.csdn.net'
    }
url = 'http://blog.csdn.net/dQCFKyQDXYm3F8rB0/article/details/78478523'
html_bytes = requests.get(url=url, headers=header)
html = html_bytes.content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
picture = soup.find('img',attrs={'class':'avatar_pic'})
pic_url_list = str(picture).split('"')
pic_url = ''
for i in pic_url_list:
    if(i.find('http')!=-1):
        pic_url+=i
print('downloading...')#开始的标志
with open('E:\\view\\'+pic_url[-5:],'wb') as f: #打开指定的文件目录
    f.write(requests.get(url=pic_url,headers=header).content) #存放图片
