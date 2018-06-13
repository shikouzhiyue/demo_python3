#!usr/bin/pyhton
# -*-coding:utf-8-*-
import requests
import re

url = 'http://www.pythonchallenge.com/pc/def/map.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
}
html = requests.get(url, headers=headers).text
string_first = re.findall(r'f000f0">(.*?)<', html, re.S)[0].replace('\n', '')

def translate(need_string):
    letter1 = 'abcdefghijklmnopqrstuvwxyz'
    letter2 = 'cdefghijklmnopqrstuvwxyzab'
    letter_1_to_2 = {}
    string_second = ''
    for letter in letter1:
        letter_1_to_2[letter] = letter1.index(letter)
    for i in need_string:
        if i in letter1:
            string_second += letter2[letter_1_to_2[i]]##对应的位置没有变化
        else:
            string_second += i
    return string_second

print(translate('map'))
