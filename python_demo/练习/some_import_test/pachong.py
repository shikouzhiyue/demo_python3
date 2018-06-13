import urllib
import urllib.request
def clear():
    print(u'内容较多，显示3秒后翻页')
    time.sleep(3)
    OS = platform.system()
    if(OS == u'Windows'):
        os.system('cls')
    else:
        os.system('clear')
def linkBaidu():
    url = r'http://www.baidu.com'
    try:
        response = urllib.request.urlopen(url)
    except urllib.URLError:
        print(u'网络地址错误')
        exit()
    with open('./baidu.txt', 'wb') as fp:
        fp.write(response.read())
    print(u'获取url信息，respons.geturl() \n: %s' % response.geturl())
    print(u'获取返回代码，respons.getcode() \n: %s' % response.getcode())
    print(u'获取返回信息，respons.getinfo() \n: %s' % response.info())
    print(u'获取的网页内容已经存入当前目录的baidu.txt中，请自行查看')
if __name__ == '__main__':
    linkBaidu()