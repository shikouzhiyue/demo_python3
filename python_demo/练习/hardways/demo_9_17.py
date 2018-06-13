'''
利用requests库爬取堆糖网
特点 多线程+上锁 字符串常用方法 页面获取方式通过函数确定
'''
import requests
import urllib.parse
import threading
#设置最大线程
thread_lock = threading.BoundedSemaphore(value=10)
'''https://www.duitang.com/napi/blog/list/by_search/?kw=%E6%A0%A1%E8%8A%B1&start=0'''


# 获取页面
def getUrl(url):
    page = requests.get(url)
    page = page.content.decode('utf-8')
    return page


# 获取多页面
def get_all_urls(name):
    pages = []
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=24'
    name = urllib.parse.quote(name)
    for index in range(0, 48, 24):
        u = url.format(name, index)
        print(u)
        page = getUrl(u)
        pages.append(page)
    return pages


# 解析方法：找到合适的链接
def find_all_imgurl(page, startpart, endpart):
    all_imgurls = []
    end = 0
    while page.find(startpart, end) != -1:
        start = page.find(startpart, end) + len(startpart)
        end = page.find(endpart, start)
        imgurl = page[start:end]
        all_imgurls.append(imgurl)
    return all_imgurls


# 将页面中的图片链接放入列表中
def img_from_url(pages):
    img_urls = []
    for page in pages:
        urls = find_all_imgurl(page, '"path":"', '"')
        img_urls.extend(urls)
    return img_urls

# 下载图片并写入
def download_imgs(url, n):
    r = requests.get(url)
    path = 'imgs/' + str(n) + '.jpg'
    with open(path, 'wb') as fl:
        fl.write(r.content)
    #解锁
    thread_lock.release()

# 主函数
def main(name):
    pages = get_all_urls(name)
    imgs_url = img_from_url(pages)
    n = 0
    for img_url in imgs_url:
        n += 1
        print('正在下载第 {} 张图片'.format(n))
        #上锁
        thread_lock.acquire()
        t = threading.Thread(target=download_imgs, args=(img_url, n))
        t.start()
    print('总共下载了 {} 张图片'.format(n))

main('校花')