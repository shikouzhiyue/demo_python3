#!usr/bin/python
# -*- coding:utf-8 -*-
strings = ['1', '11']

# 计算1-30的元素
for i in range(1, 31):
    # 计数器重置
    j = 0
    temp = ''
    # 当计数器j小于当前元素的长度时（即当前元素的长度还未计算完毕时）这个循环很厉害，我自己写不出来
    while j < len(strings[i]):
        count = 1
        # 当计数器j小于前一个元素的长度时且strings[i][j]==strings[i][j+1]
        while j < (len(strings[i]) - 1) and (strings[i][j] == strings[i][j + 1]):
            j = j + 1
            count = count + 1
        temp = '%s%d%c' % (temp, count, strings[i][j])
        j = j + 1
    strings.append(temp)
# for i in strings:
#     if i == 10:
#         break
#     else:
#         print(i)
print(len(strings[30]))
