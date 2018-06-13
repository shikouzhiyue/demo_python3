# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 保存爬取结果
import time
import os
from urllib import request


class QiushiPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d', time.localtime())
        fileName = today + '.txt'
        imgDir = 'IMG'
        if os.path.isdir(imgDir):
            pass
        else:
            os.mkdir(imgDir)
        with open(fileName, 'a', encoding='utf-8') as fp:
            fp.write('-' * 50 + '\n' + '*' * 50 + '\n')
            fp.write("author:%s\n" % (item['author']))
            fp.write("content:%s\n" % (item['content']))
            try:
                imgUrl = "http:" + item['img'][1]  # [0]表示的是头像，[1]中的才是内容里的图片
            except IndexError:
                pass
            else:
                imgName = os.path.basename(imgUrl)
                fp.write("img:\t %s\n" % (imgName))
                imgPathName = imgDir + os.sep + imgName  # os.sep是文档目录的分割线
                with open(imgPathName, 'wb') as fp1:
                    response = request.urlopen(imgUrl)
                    fp1.write(response.read())
            fp.write("fun:%s\t  talk:%s\n" % (item['funNum'], item['talkNum']))
            fp.write('*' * 50 + '\n' + '-' * 50 + '\n' * 5)
            time.sleep(1)
        return item