import os
def ss(str):
    a=[x for x in os.listdir('.') if os.path.isfile(x) and str in x ]
    for x in a:
        print(os.path.abspath(x))
    b=[os.path.abspath(x) for x in os.listdir('.') if os.path.isdir(x)]
    for x in b:
        a=[q for q in os.listdir('.') if os.path.isfile(os.path.join(x,q) and str in q)]
        for x in a:
            print(os.path.abspath(a))
print(ss(input('输入你要查找的文件')))