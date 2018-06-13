#-*- coding：utf-8 -*-
import scrapy
from agentxixi.items import AgentxixiItem


class xixiSpider(scrapy.Spider):
    name = 'xixiSpider'
    allowed_domains = ['xicidaili.com']
    wds = ['nn', 'nt', 'wn', 'wt']
    pages = 10
    start_urls = []
    count = 0
    for type in wds:
        for i in range(1, pages + 1):
            start_urls.append('http://www.xicidaili.com/' + type + '/' + str(i))

    def parse(self, response):
        subSelector = response.xpath('//tr[@class=""]|//tr[@class="odd"]')
        items = []
        for sub in subSelector:
            item = AgentxixiItem()
            item['ip'] = sub.xpath('.//td[2]/text()').extract()[0]
            item['port'] = sub.xpath('.//td[3]/text()').extract()[0]
            item['type'] = sub.xpath('.//td[5]/text()').extract()[0]
            if sub.xpath('.//td[4]/a/text()'):
                item['location'] = sub.xpath('//td[4]/a/text()').extract()[0]
            else:
                item['location'] = sub.xpath('.//td[4]/text()').extract()[0]
            item['protocol'] = sub.xpath('.//td[6]/text()').extract()[0]
            item['source'] = 'xicidaili'
            self.count += 1
            item['id'] = str(self.count)
            items.append(item)
        return items