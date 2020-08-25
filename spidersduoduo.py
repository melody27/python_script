import requests
import re 
import threading
import queue
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
def alllianjie():#抓取到首页所有的展开列表链接
    r=requests.get('http://www.win4000.com/meitu.html',headers=headers)
    r.encoding='utf-8'
    all_lianjie=re.findall('http://www.win4000.com/meinvtag\w*\_\w*.html',r.text)
    return jieshou(all_lianjie)
    

def jieshou(ii):
    zzilist=[]
    for x in ii:
        z=requests.get(x,headers=headers)
        z.encoding='utf-8'
        f=re.findall('http://www.win4000.com/meinvtag\w*\_\w*.html',z.text)
        for x in f:
            zzilist.append(x)
    return zzilist


def kkp(lianjie):
    r=requests.get(lianjie,headers=headers)
    r.encoding='utf-8'
    fing=re.findall('http://www.win4000.com/meinv\d{6}.html',r.text)
    for x in fing:
        down(x)
    
def spiders():#抓取首页的所有链接
    dizhi='http://www.win4000.com/meitu.html'
    r=requests.get(dizhi,headers=headers)
    r.encoding='utf-8'
    # print(r.text)
    lianjielist=re.findall('http://www.win4000.com/meinv\d{6}.html',r.text)
    return lianjielist
def down(biaodizhi):#判断链接的附近图片是否可用
    for x in range(1,21):
        z=biaodizhi.replace(".html","_%s.html" %x)
        r=requests.get(z,headers=headers)
        if r.status_code == 200:
            r.encoding='utf-8'
            download(r)
def download(r):#寻找该地址的图片并下载
    xunzhao=re.findall(r'http://pic1.win4000.com/pic/\w/\w{1,3}/\w{1,20}.jpg',r.text)   #http://pic1.win4000.com/pic/\d/\d{2}/\d{2,15}.jpg
    for x in xunzhao:
        print('计算x',x)
        img=requests.get(x,headers=headers)
        img_name=x.split('/')[-1]
        with open("pachong/" + img_name, 'wb') as f:
            f.write(img.content)
            print("%s saved" % img_name)
if __name__=='__main__':
    jihe=list(set(spiders()))
    print('这里是集合',jihe)
    q=queue.Queue()
    xianchengchangdu=10
    for x in jihe:
        q.put(x)
    while not q.empty():
        tt=[]
        for x in range(xianchengchangdu):
            tt.append(threading.Thread(target=down,args=(q.get(),)))
        # print(tt)
        for x in tt:
            x.start()
        for x in tt:
            x.join()
    c=alllianjie()
    w=queue.Queue()
    for x in c:
        w.put(x)
    while not w.empty():
        he=[]
        for x in range(len(c)):
            he.append(threading.Thread(target=kkp,args=(w.get(),)))
        for x in he:
            x.start()
        for x in he:
            x.join()