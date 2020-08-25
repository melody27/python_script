import threading
from threading import Thread
import time
import queue
import requests
import re
import os
import json
from multiprocessing import Process


class bilibili(Process):
    def __init__(self,page):
        Process.__init__(self)
        self.url = 'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num={}&page_size=20'
        self.page = str(page)
        self.img_and_title = None
        self.path = '/tmp/test'
    
    def run(self):
        self.page_get(self.page)

    def page_get(self,page):
        r = requests.get(url=self.url.format(page))
        r_dict = eval(r.text)
        self.Filling(r_dict)


    def Filling(self,Page_dict):

        img_and_title = {}
        for User_lists in Page_dict['data']['items']:
            img_and_title[User_lists['user']['name']] = []
            for img_list in User_lists['item']['pictures']:
                img_and_title[User_lists['user']['name']].append(img_list['img_src'])
        self.img_and_title = img_and_title
        # print(self.img_and_title)
        self.down()


    def down(self):
        action_dict = self.img_and_title

        down_list = []
        for title in action_dict:
            try:
                path = self.path+'/'+str(title)
                # print(path)
                os.mkdir(path)
            except FileExistsError as identifier:
                continue
            for img_url in action_dict[title]:
                print("开始装载：img_url：{img_url}".format(img_url=img_url))
                # down_list.append(Page_down_load(img_url,path))
                # Page_down_load(img_url,path).start()

                t = Page_down_load(img_url,path)
                t.start()
                down_list.append(t)
            print("存活的线程数：",threading.active_count())
            # for x in down_list:
            #     x.start()
            # for x in down_list:
                # x.join()    
            
def jisuan(url,path):
    print(url,path)
            


class Page_down_load(threading.Thread):
    def __init__(self,url,path):
        threading.Thread.__init__(self)
        self.img_url = url
        self.path = path+'/'+str(time.time())+'.jpg'
        self.headers = {
            "Host": "api.vc.bilibili.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://h.bilibili.com/eden/picture_area",
            "Origin": "https://h.bilibili.com"
        }


    def run(self):
        try:
            r = requests.get(url=self.img_url)
            print("简单输出一下url:{}".format(self.img_url))
            with open(self.path,'wb') as f:
                f.write(r.content)
        except:
            print(self.img_url)
        

    




class Page(threading.Thread):

    def __init__(self,page):
        threading.Thread.__init__(self)
        self.url = 'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num={}&page_size=20'
        self.page = str(page)
    
    def run(self):
        pass



if __name__ == "__main__":
    start_time = time.time()
    # page_1 = bilibili(0)
    b_list = []
    for i in range(1):                 # 多进程的操作
        b = bilibili(i)
        b.start()
        b_list.append(b)
    for b in b_list:
        b.join()


    print("执行时间：{}".format((time.time()-start_time)))
