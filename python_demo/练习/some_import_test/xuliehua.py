#E:\课件\大四\最终版本\图片
'''with open(r'E:\课件\大四\最终版本\图片\校徽.jpg', 'rb') as f:
    print(f.read())'''
import pickle
d = dict(name="zhoaying", age=22, school="dongbeidaxue")
with open("E:\\python\\书籍\\练习\\lianxi.txt",'rb') as f:
    d = pickle.load(f)
    print(d)