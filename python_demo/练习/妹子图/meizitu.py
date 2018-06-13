#!usr/bin/python
# -*- coding:utf-8 -*-
##最开始的版本就是这样，单纯的按顺序执行
import requests
from bs4 import BeautifulSoup
import os

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
    'Cache-Control': 'max-age=0'
    ##由于只携带请求头得到的是乱码，观察对比之后，all页面比别的页面多的参数就是这一个，故而加上
}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

all_url = 'http://www.mzitu.com/all/'
start_html = requests.get(all_url, headers=headers1)
# print(start_html.text)
##content是二进制的数据，一般用于下载图片，视频，音频等多媒体内容，
##对于打印网页内容使用text
Soup = BeautifulSoup(start_html.text, 'lxml')
a_list = Soup.find('div', class_='all').find_all('a')
for a in a_list:  ##得到总的相册，然后遍历
    title = a.get_text()  ##获取a标签中的文本
    href = a['href']  ##获取a标签中的href属性
    if href[-1].isdigit():
        # print(href)
        html = requests.get(href, headers=headers2)
        html_Soup = BeautifulSoup(html.text, 'lxml')
        max_page = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
        ##得到总共的页数
        for page in range(1, int(max_page) + 1):  ##得到个人的总相册，然后遍历
            page_url = href + '/' + str(page)
            img_html = requests.get(page_url, headers=headers2)
            img_Soup = BeautifulSoup(img_html.text, 'lxml')
            img_url = img_Soup.find('div', class_='main-image').find('img')['src']
            name = img_url[-9:-4]
            headers3 = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }
            headers3['Referer'] = page_url
            ##从下载的图片失败可以知道，图片存在防盗链，通过比较以及查资料可以发现，该网站采用的防盗原理是Referer
            ##也就是网页从哪里来，只有从指定页面来才能下载
            # print(headers3)
            img = requests.get(img_url, headers=headers3)
            # print('开始')
            with open(name + '.jpg', 'ab') as f:
                f.write(img.content)
            break
            # print(page_url)
        break


def mkdir(self, path):
    path = path.strip()
    isExists = os.path.exists(os.path.join('D:\photo\mzitu', path))
    if not isExists:
        print(u'创建了一个', path, u'的文件夹')
        os.mkdir(os.path.join('D:\photo\mzitu', path))
        os.chdir(os.path.join('D:\photo\mzitu', path))
        return True
    else:
        print(u'文件夹以及存在')
        return False
