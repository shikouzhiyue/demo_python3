#使用代理
# 代理Ip
import urllib.request
import random
#访问网址
url = 'http://www.baidu.com/'
#代理IP列表
iplist = ['110.73.1.179:8123']
#创建ProxyHandler
proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})
#创建Opener
opener = urllib.request.build_opener(proxy_support)
#添加 User Angent
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
#安装OPener
urllib.request.install_opener(opener)
#使用自己安装好的Opener
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)


#设置user-agent
'''先看下urllib.request.Request()

1
从上图可以看出，在创建Request对象的时候，可以传入headers参数。
因此，想要设置User
Agent，有两种方法：

1.
在创建Request对象的时候，填入headers参数(包含User
Agent信息)，这个Headers参数要求为字典；

2.
在创建Request对象的时候不添加headers参数，在创建完成之后，使用add_header()
的方法，添加headers。'''
# -*- coding: UTF-8 -*-
#方法一
from urllib import request

if __name__ == "__main__":
    #以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://www.csdn.net/'
    head = {}
    #写入User Agent信息
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
 #创建Request对象
    req = request.Request(url, headers=head)
    #传入创建好的Request对象
    response = request.urlopen(req)
    #读取响应信息并解码
    html = response.read().decode('utf-8')
    #打印信息
    print(html)

#方法二
# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    #以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://www.csdn.net/'
    #创建Request对象
    req = request.Request(url)
    #传入headers
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')
    #传入创建好的Request对象
    response = request.urlopen(req)
    #读取响应信息并解码
    html = response.read().decode('utf-8')
    #打印信息
    print(html)