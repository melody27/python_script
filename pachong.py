#这个py文件主要作用是爬虫爬简述上的内容
import requests
url='https://www.jianshu.com/'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
r=requests.get(url,headers=headers)
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.content,"html.parser")
#r.content.decode()     这两句中这句比较乱下面这句得到的html代码比较整洁
#print(r.content.decode())      但是两个都是输出一样的
#content = soup.find_all('div',id="list-container")
listcontainer=soup.find('div',id='list-container')
listcontainer.encoding='utf-8'
li=listcontainer.find_all('li')
k=open('C:/Users/11547/test.txt','a')#这里我之前写的是w
for item in li:
        z=item.find(class_='title').string
        print(z)
        f=item.find(class_='abstract').string
        print(f)
        m=item.find(class_='nickname').string
        print(m)
        # k.write(str(z))这里注释掉的是我自己写的
        # k.write('\r\n')
        # k.write(str(f))
        # k.write('\r\n')
        # k.write('\r\n')
        # k.write(str(m))
        # k.write(' ------------------------------------------------------------------------ ')
        # k.write('\r\n')
        # k.write('\r\n')
        # k.write('\r\n')
        write_string = ""
        write_string += str(z) + "\n"
        write_string += str(f).strip() + "\n"
        write_string += str(m) + "\n"
        write_string += "-"*15 + "\n"

        k.write(write_string)
k.close()