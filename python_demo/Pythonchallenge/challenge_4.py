# import requests
#
# import re
#
# url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
# url_first = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
# }
# html = requests.get(url_first, headers=headers).text
# # print(html)
# string_first = re.findall(r'nothing is (.*)', html)[0].strip()
# # while string_first.isdigit():
# #     url_second = url_first.split('=')[0] + '=' + string_first
# #     # print(url_second)
# #     html = requests.get(url_second, headers=headers).text
# #     string_first = re.findall(r'nothing is (.*)', html)[0].strip()
# #     print(string_first)
# # print(string_first)
# # string_second = ''.join(re.findall(pattern,string_first))t(string_first)
# url_before = url[:-len(url.split('/')[-1])]
# print(url_before +'peak.html')
import urllib.request
import re


def next_page(p):
    text = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % p).read().decode(
        'utf-8')
    m = re.search('and the next nothing is ([0-9]+)', text)
    if not m:
        print(text)
    return m.group(1)


p = 12345

for i in range(1, 400):
    print(" 第%s次运行" % i, end="")
    p = next_page(p)
    print(p)
