import requests
import re

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
}
html = requests.get(url, headers=headers).text
string_first = re.findall(r'.*<!--(.*?)-->', html, re.S)[0].strip()
string_second = ''.join([char for char in string_first if char.isalpha()])
url_before = url[:-len(url.split('/')[-1])]
print(url_before +string_second+'.html')
