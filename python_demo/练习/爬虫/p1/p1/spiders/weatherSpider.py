#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Python爬虫 爬取天气 然后存储为 TXT，json ，mysql
import scrapy
from p1.items import P1Item

class weatherSpider(scrapy.spiders.Spider):
    name = "wuhanweather"
    allowed_domains = ["tianqi.com"]
    citys = ['wuhan', 'zhengzhou']
    start_urls = []
    for city in citys:
        start_urls.append('httP://' + city + '.tianqi.com/')

    def parse(self, response):
        subSelector = response.xpath('//div[@class="tqshow1"]')
        items = []
        for sub in subSelector:
            item = P1Item()
            cityDates = ''
            for cityDate in sub.xpath('./h3//text()').extract():
                cityDates += cityDate
            item['cityDate'] = cityDates
            item['week'] = sub.xpath('./p//text()').extract()[0]
            item['img'] = sub.xpath('./ul/li[1]/img/@src').extract()[0]
            temps=''
            for temp in sub.xpath('./ul/li[2]//text()').extract():
                temps += temp
            item['temperature'] = temps
            item['weather'] = sub.xpath('./ul/li[3]//text()').extract()[0]
            item['wind'] = sub.xpath('./ul/li[4]//text()').extract()[0]
            items.append(item)
            yield item