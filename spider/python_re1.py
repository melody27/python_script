import re 

test = "This is the last one"

res = re.match('(.*) is (.*?)',test,re.M | re.I)

if res :
    print('res：',res)
    print('res.group()：',res.group())      #match匹配的对象要是用group()或groups()来取
    print('res.group(1)：',res.group(1))
    print('res.group(2)：',res.group(2))
    print('res.groups()：',res.groups())    #search的使用方法和match基本相同，只是match
                                             #只匹配字符串的开始，不匹配的话返回None。
                                             #而search会匹配整个字符串，不匹配的话也会返回None
else:
    print('not match')

