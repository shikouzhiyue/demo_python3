with open('test.jpg', 'rb') as fp:
    with open('test2.jpg', 'wb') as fo:
        fo.write(fp.read())
