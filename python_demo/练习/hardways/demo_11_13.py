import urllib.request
from bs4 import BeautifulSoup


url = "http://www.tybai.com/"
html_bytes = urllib.request.urlopen(url).read()
html = html_bytes.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
#找到想要的图片所在的标签
info = soup.find_all('script', attrs={'type': 'text/javascript'})
#设置一个图片链接的集合，存储图片地址
pics = []
for i in info:
    if i.get_text():#删除标签内没有文本的标签
        a = str(i.get_text())#将其转化成字符串格式
        b = a.split('"\\')#分割字符串，找到图片链接的位置
        for j in b:
            j = j[:19]#选择只包含图片链接的文本
            if j.find('jpg')!=-1:#将不是图片的文本过滤
                pics.append('http://www.tybai.com'+j.replace('\\',''))#替换文本中不合适的字符，
                # 并加上前缀，添加到列表中
        break
for pic in pics:
    print('downloading...')#每一次开始的标志
    with open('E:\\view\\'+pic[-5:],'wb') as f: #打开指定的文件目录
        f.write(urllib.request.urlopen(pic).read()) #存放图片
