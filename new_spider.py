import requests
import threading
import re
import queue
# from lxml import etree as et
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

def spider():
    url = "https://m.fang.com/esf/cd/"
    print('开始进行请求')

    r = requests.get(url,headers=headers)
    if r.status_code == 200:
        parser(r)
        
def parser(taget):
    sou = BeautifulSoup(taget.content,"html.parser")
    soup = sou.find('ul',id="content")
    tag = soup.find_all('p')
    tag.encoding='utf-8'
    i=0
    write = open('d:/python/python项目目录/pachong/tt.csv','a')
    for x in tag:
        z = x.text
        z += "\n"
        print(x.text)
        print(br)
        write.write(z)
    write.close()
        

#  sou = BeautifulSoup(taget.content,"html.parser")
#     soup = sou.ul
#     tag = soup.find_all('p')
#     print(tag)

if __name__ == "__main__":
    spider()