import requests
from bs4 import BeautifulSoup
import re
import queue
import threading
import hashlib


def encrypt(url):
    m = hashlib.md5()
    m.update(url.encode("utf-8"))
    return m.hexdigest()


def ff(n):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    page='http://desk.zol.com.cn/meinv/%s.html'%n
    print("Starting Spider: " + page)
    requests_1=requests.get(page,headers=headers)
    
    if requests_1.status_code!=200:
        print("该页面不存在")
        return 
        # raise Exception("该页面不存在")
    requests_1.encoding = requests_1.apparent_encoding #
    re_1 = re.findall(r'https://desk-fd.zol-img.com.cn/t_s208x130c5/\w{1,5}/\w{3}/\w{2}/\w{2}/\w*.jpg', requests_1.text)
    len_re_1=len(re_1)
    print('所有的长度',len_re_1)
    for x in re_1:
        with open('imgsave/' + encrypt(x) + ".jpg",'wb')as f:
            try:
                requests_2 = requests.get(x, headers=headers)
                print(x + " saved!")
                f.write(requests_2.content)
            except requests.exceptions.ConnectionError as identifier:
                print('Error %s' % identifier)
            
if __name__=='__main__':
    que_1=queue.Queue()
    xianzhi=10
    for x in range(1,100):
        que_1.put(x)
    while not que_1.empty():
        try:
            list_1=[]
            for i in range(xianzhi):
                list_1.append(threading.Thread(target=ff,args=(que_1.get(),)))
            for x in list_1:
                x.start()
            for x in list_1:
                x.join()
        except KeyboardInterrupt:
            exit("keyboard interrupt")
        
