#!usr/bin/python
# -*- coding:utf-8 -*-
f = open('evil2.gfx', 'rb+')
content = f.read()
for i in range(5):
    with open('%d.jpg' % i, 'wb') as file:
        file.write(content[i::5])
print('done')
