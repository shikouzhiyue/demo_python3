import time
import random
import requests


def get_time():
    timerandom = random.randint(100, 999)
    nowtime = int(time.time())
    return str(nowtime) + str(timerandom)

def get_url(url,postdata):
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'sp0.baidu.com',
        'Referer': 'https://www.baidu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0'
    }
    html_bytes=requests.get(url,headers=header,params=postdata)
    return html_bytes.content

if __name__ == "__main__":
    url='http://www.baidu.com/s?'
    keywords=input('想要查询的关键字：')
    postdata = {
        '_': get_time(),
        'bs': keywords,
        'cb': 'jQuery110206323874822111253_1510905734672',
        'csor': '9',
        'json': '1',
        'p': '3',
        'pbs': keywords,
        'req': '2',
        'sid': '1446_21125_17001_20928',
        'wd': keywords
    }
    html_bytes = get_url(url, postdata)
    html = html_bytes.decode("utf-8", "ignore")
    print(html)