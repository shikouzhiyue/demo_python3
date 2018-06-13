#!usr/bin/python
# -*- coding:utf-8 -*-
import gzip, difflib
import binascii

# same : hex/bin/html
# left : fly
# right : butter
#
# 读取文件中的数据。我们需要读取字符串，所以是‘rt'，文本类型读取模式
ff = gzip.open('./18/deltas.gz', 'rt')
deltas = ff.read()
ff.close()
# 按行分成列表
deltas = deltas.splitlines()
left, right = [], []
# 吧左右两个图片字符串分别保存在两个列表中
for row in deltas:
    # 从0开始每一行前一段字符串长54，中间隔了两个空格，后一段开始为56
    left.append(row[:53])
    right.append(row[56:])
''''' 
class difflib.Differ.compare(a,b)和difflib.ndiff（a，b)一样 
Code      Meaning 
'- '      仅在片段1中存在 
'+ '      仅在片段2中存在 
' '       片段1和2中都存在 
'? '      存在疑问的 
eg:
a = '89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00   89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00'
b = '75 55 14 aa 9c a8 69 a5 86 1a 86 a0 00 28 e8 94 72 8b   75 55 16 2e b2 23 05 d5 52 9b 44 cb 8b 3b 10 a0 e5 ee'

print(difflib.ndiff(a[:53],a[56:]))
['89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00'] ['89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00']
['  89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00']

print(difflib.ndiff(b[:53],b[56:]))
['75 55 14 aa 9c a8 69 a5 86 1a 86 a0 00 28 e8 94 72 8b'] ['75 55 16 2e b2 23 05 d5 52 9b 44 cb 8b 3b 10 a0 e5 ee']
['- 75 55 14 aa 9c a8 69 a5 86 1a 86 a0 00 28 e8 94 72 8b', '+ 75 55 16 2e b2 23 05 d5 52 9b 44 cb 8b 3b 10 a0 e5 ee']
'''
# 查找不同的结果
diff = list(difflib.ndiff(left, right))
# print(diff)

# 使用zip函数将不同类放在不同的图片之中
png = ['same.png', 'right.png', 'left.png']
pngs = zip(png, [''.join(row[2:] for row in diff if i == row[0]) for i in ' +-'])

# 写入到不同的图片
for filename, data in pngs:
    # 去掉每一行字符串之间的空格
    strs = data.replace(' ', '')
    # 把十六进制的字符串转为二进制数据bytes类型
    strs_unhex = binascii.unhexlify(strs)
    open(filename, 'wb').write(strs_unhex)