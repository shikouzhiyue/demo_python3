#!usr/bin/python
# -*- coding:utf-8-*-
#改进版，将代码变成函数，类
import requests
from bs4 import BeautifulSoup
import os
import time
import random


class mzitu():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
        }

    def all_url(self, url):
        self.headers['Cache-Control'] = 'max-age=0'
        html = self.request(url)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            href = a['href']
            if href[-1].isdigit():
                print(u'开始保存 ', title)
                path = str(title).replace('?', '_')
                self.makedir(path)
                self.html(href)
                time.sleep(2.5 + random.random() * 3)

    def html(self, href):
        html = self.request(href)
        self.headers['Referer'] = href
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, 2):
            page_url = href + '/' + str(page)
            self.img(page_url)

    def img(self, page_url):
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url):
        name = img_url[-9:-4]
        img = self.request(img_url)
        with open(name + '.jpg', 'ab') as f:
            f.write(img.content)

    def makedir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join('D:\photo\mzitu', path))
        if not isExists:
            print(u'创建了一个', path, u'的文件夹')
            os.mkdir(os.path.join('D:\photo\mzitu', path))
            os.chdir(os.path.join('D:\photo\mzitu', path))
            # return True
        else:
            print(u'文件夹已存在')
            # return False

    def request(self, url):
        content = requests.get(url, headers=self.headers)
        return content


if __name__ == '__main__':
    Mzitu = mzitu()
    Mzitu.all_url('http://www.mzitu.com/all')
