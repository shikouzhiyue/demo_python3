from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from qiushi import userAgents


class CustomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = userAgents.pcUserAgent.get('qiubai')
        #      ua="Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        request.headers.setdefault('User-Agent', ua)


class CustomProxy(object):
    def process_request(self, request, spider):
        # 这里的代理可能要跟着换，可以去西刺代理网里找最新的代理
        request.meta['proxy'] = '219.142.211.165:8118'