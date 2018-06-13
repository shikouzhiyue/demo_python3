#定义如何爬取

import scrapy
from qiushi.items import QiushiItem


class QiushiSpider(scrapy.Spider):
    name = "qiushiSpider"
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/hot/']


    def parse(self, response):
        subSelector = response.xpath('//div[@class="article block untagged mb15"and @id]')
        items = []
        for sub in subSelector:
            item = QiushiItem()
            item['author'] = sub.xpath('.//h2/text()').extract()[0]
            item['content'] = sub.xpath('.//div[@class="content"]/span/text()').extract()[0]
            item['img'] = sub.xpath('.//img/@src').extract()
            item['funNum'] = sub.xpath('.//i[@class="number"]/text()').extract()[0]
            try:
                item['talkNum'] = sub.xpath('.//i[@class="number"]/text()').extract()[1]
            except IndexError:
                item['talkNum'] = '0'
            items.append(item)
        return items