import requests
import threading
from bs4 import BeautifulSoup
import threading,time,os
from urllib import request
import re
def diaoyong(url):
    print(url)
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.content,"html.parser")
    the_content=soup.find('div',id='content')
    img_p=the_content.find_all('img')
    root=r"D:/python/pachong"
    imglist=[]
    os.chdir('D:/python/pachong')
    for x in img_p:
        src = x.attrs['src']#读取字典的src
        #print(src)#查到这了
        imglist.append(src)
    for i, v in enumerate(imglist):
        print('v的值为',v,threading.current_thread().name)
        # if(re.match(r'\.*\\x\s+\.jpg$',v)):
        #     continue
        # else:
        u=(threading.current_thread().name+str(i + 1) + '.jpg')
        try:
            request.urlretrieve(v,u)
        except BaseException as identifier:
            print('出错')
# def zhengzhe(addr):这个正则表达式没有用上
#     if(re.match(r'\x\s+\.jpg$',addr)!=None):
#         return False
#     return True
if __name__=='__main__':
    start=time.time()
    t1=threading.Thread(target=diaoyong,name='线程1',args=('http://hotpics.cc/category/milfs-pics/page/2/',))
    t2=threading.Thread(target=diaoyong,name='线程2',args=('http://hotpics.cc/category/milfs-pics/page/4/',))
    t3=threading.Thread(target=diaoyong,name='线程3',args=('http://hotpics.cc/category/milfs-pics/page/3/',))
    # diaoyong('http://hotpics.cc/category/milfs-pics/page/2/')
    t3.start()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t3.join()
    end=time.time()
    print('hellow')
    print(start-end)