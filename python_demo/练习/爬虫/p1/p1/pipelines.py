# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os.path
import urllib.request

class P1Pipeline(object):
    def __init__(self):
        pass
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today + '.txt'
        with open(fileName, 'a', encoding='utf-8') as fp:
            fp.truncate()
            fp.write(item['cityDate'] + '\t')
            fp.write(item['week'] + '\t')
            imgName = os.path.basename(item['img'])
            fp.write(imgName + '\t')
            if os.path.exists(imgName):
                pass
            else:
                with open(imgName, 'wb') as fd:
                    response = urllib.request.urlopen(item['img'])
                    fd.write(response.read())
            fp.write(item['temperature'] + '\t')
            fp.write(item['weather'] + '\t')
            fp.write(item['wind'] + '\n\n')
            time.sleep(1)
        return item
