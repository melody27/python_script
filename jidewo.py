'''
import os 
s=input('输入你想查找的文件名')
z=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.split(x)[1]==s]
print(z)
print(type(z))
'''
import os


def search(path, string):
    for x in os.listdir(path):
        sub_path = os.path.join(path, x)
        if os.path.isdir(sub_path):
            search(sub_path, string)
        if os.path.isfile(sub_path) and string in x:
            print(sub_path)


search('.', '1')