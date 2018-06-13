import threading
import urllib.request
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
'''
加入线程后的两种方式
第一种使用threading
创建线程池，将线程增加到线程池内，开始执行线程，
第二种使用ThreadPoolExecutor
设置最大线程数，将任务加入线程中去。
'''
url="http://www.tybai.com/"
pics = []
def get_urls(url):
    html_bytes = urllib.request.urlopen(url).read()
    html = html_bytes.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # 找到想要的图片所在的标签
    info = soup.find_all('script', attrs={'type': 'text/javascript'})
    # 设置一个图片链接的集合，存储图片地址
    for i in info:
        if i.get_text():  # 删除标签内没有文本的标签
            a = str(i.get_text())  # 将其转化成字符串格式
            b = a.split('"\\')  # 分割字符串，找到图片链接的位置
            for j in b:
                j = j[:19]  # 选择只包含图片链接的文本
                if j.find('jpg') != -1:  # 将不是图片的文本过滤
                    pics.append('http://www.tybai.com' + j.replace('\\', ''))  # 替换文本中不合适的字符，并加上前缀，添加到列表中
            return pics

def downloading(pic_url):
    print('downloading...')  # 每一次开始的标志
    with open('E:\\view\\' + pic_url[-5:], 'wb') as f:  # 打开指定的文件目录
        f.write(urllib.request.urlopen(pic_url).read())  # 存放图片

# #创建线程池
# threadpool = []
# for pic_url in get_urls(url):
#     # 定义线程
#     th = threading.Thread(target=downloading, args=(pic_url,))#注意，这里如果只有一个参数，
#                                                      #一定要加，这里传入的是一个数组变量参数
#     # 将线程加入线程池
#     threadpool.append(th)
# # 开始线程
# for th in threadpool:
#     th.start()
# # 等待所有线程运行完毕
# for th in threadpool:
#     th.join()
pool = ThreadPoolExecutor(max_workers=6)
for pic_url in get_urls(url):
    pool.submit(downloading,pic_url)