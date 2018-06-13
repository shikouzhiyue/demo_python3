#!usr/bin/python
# -*- coding:utf-8-*-
from bs4 import BeautifulSoup
import os
from Download import down
from pymongo import MongoClient
import datetime
import time
import random


class mzitu():
    def __init__(self):
        client = MongoClient()  ##与MongDB建立连接（这是默认连接本地MongDB数据库）
        db = client['meinvxiezhenji']  ## 选择一个数据库
        self.meizitu_collection = db['meizitu']  ##在meizixiezhenji这个数据库中，选择一个集合
        self.title = ''  ##用来保存页面主题
        self.url = ''  ##用来保存页面地址
        self.img_urls = []  ##初始化一个 列表  用来保存图片地址

    def all_url(self, url):
        html = down.get(url, 3)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            href = a['href']
            if href[-1].isdigit():
                self.title = title  ##将主题保存到self.title中
                print(u'开始保存：', title)
                path = str(title).replace("?", '_')
                self.mkdir(path)
                os.chdir("D:\mzitu\\" + path)
                self.url = href  ##将页面地址保存到self.url中
                if self.meizitu_collection.find_one({'主题页面': href}):  ##判断这个主题是否已经在数据库中、不在就运行else下的内容，在则忽略。
                    print(u'这个页面已经爬取过了')
                else:
                    print(href)
                    self.html(href)

    def html(self, href):
        html = down.get(href, 3)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        print(max_span)
        page_num = 0  ##这个当作计数器用 （用来判断图片是否下载完毕）
        for page in range(1, (int(max_span)) // 10 + 1):
            page_num = page_num + 1  ##每for循环一次就+1  （当page_num等于max_span的时候，就证明我们的在下载最后一张图片了）
            page_url = href + '/' + str(page)
            self.img(page_url, max_span, page_num)  ##把上面我们我们需要的两个变量，传递给下一个函数。

    def img(self, page_url, max_span, page_num):  ##添加上面传递的参数
        img_html = down.get(page_url, 3)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.img_urls.append(img_url)  ##每一次 for page in range(1, int(max_span) + 1)获取到的图片地址都会添加到 img_urls这个初始化的列表
        if (int(max_span) // 10) + 1 == page_num:  ##我们传递下来的两个参数用上了 当max_span和Page_num相等时，就是最后一张图片了，最后一次下载图片并保存到数据库中。
            self.save(img_url)
            post = {  ##这是构造一个字典，里面有啥都是中文，很好理解吧！
                '标题': self.title,
                '主题页面': self.url,
                '图片地址': self.img_urls,
                '获取时间': datetime.datetime.now()
            }
            self.meizitu_collection.save(post)  ##将post中的内容写入数据库。
            print(u'插入数据库成功')
        else:  ##max_span 不等于 page_num执行这下面
            self.save(page_url, img_url)

    def save(self, page_url, img_url):
        name = img_url[-9:-4]
        print(u'开始保存：', img_url)
        img = down.get_img(img_url, 3, page_url)
        time.sleep(1 + random.random() * 3)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\mzitu", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\mzitu", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False


if __name__ == '__main__':
    Mzitu = mzitu()  ##实例化
    Mzitu.all_url('http://www.mzitu.com/all')  ##给函数all_url传入参数  你可以当作启动爬虫（就是入口）
