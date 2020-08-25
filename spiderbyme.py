import requests
import time
import re
import queue
import threading

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}



def spider(page):
    dizhi='https://www.7160.com/meinvmingxing/list_5_%s.html' % page
    r=requests.get(dizhi,headers=headers)
    if  r.status_code==200:
        relist=re.findall('https://img.lovebuy99.com/uploads/\d{6}/.*?.jpg',r.text)
        print('获取到的图片地址组',relist)
    for x in relist:
        download(x)



def download(sss):
    img=requests.get(sss)
    img_name=sss.split("/")[-1]
    if img.status_code==200:
        with open('pachong/' + img_name,'wb')as f:
            f.write(img.content)
    print('正在写入',img_name)
    #http://t1.hxzdhn.com/uploads/tu/201906/9999/rn286718a912.jpg
    #http://t1.hxzdhn.com/uploads/150415/1-1504151I351N2.jpg




if __name__=='__main__':
    q=queue.Queue()
    for x in range(1,316):
        q.put(x)
    while not q.empty():
        threading_list=[]
        for z in range(10):
            if not q.empty():
                threading_list.append(threading.Thread(target=spider,args=(q.get(),)))
        for x in threading_list:
            x.start()
        for x in threading_list:
            x.join()
        