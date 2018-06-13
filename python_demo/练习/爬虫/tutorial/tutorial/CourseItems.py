__author__ = ' HeFei University of Technology Qian Yang email：1563178220@qq.com'
# -*- coding:utf-8 -*-
import scrapy
class MovieItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    rate = scrapy.Field()
    quote = scrapy.Field()