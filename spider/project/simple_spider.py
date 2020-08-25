import requests
import re
import threading
import queue
import urllib3
import re
from bs4 import BeautifulSoup
import json
urllib3.disable_warnings()


def index(s):

    url = "https://www.luolidao.com//wp-admin/admin-ajax.php?action=zrz_load_more_posts"
    header = {
        "Referer":"https://www.luolidao.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
    }
    data = {
        "type" : "index",
        "paged" : s
    }

    r = requests.post(url,data=data,headers=header,verify=False)
    r.encoding="utf-8"
    z = json.loads(r.text)
    r_text = str(z["msg"])
    # print(r_text)
    r_text = re.sub(r'\\',"",r_text)
    r_text = re.findall(r'https://www.luolidao.com/.*/.*/\d+.html',r_text)
    
    for x in r_text:
        spider(x)
    
def spider(r):

    url = str(r)
    headers = {
        "Referer":"https://www.luolidao.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
    }

    r = requests.get(url,headers=headers)
    r.encoding="utf-8"
    img_url = re.findall(r'https://www.luolidao.com/wp-content/uploads/\d{4}/\d{1,2}/.{1,7}.jpg',r.text)
    
    for x in img_url:
        img_content = requests.get(x)
        img_save_name = img_content.url.split("/")[-1]

        with open("/root/桌面/blog/python项目目录/spider/img/" + img_save_name, mode="wb") as f:
            f.write(img_content.content) 
            print("下载完成%s"% img_save_name)
    

if __name__ == "__main__":
    que = queue.Queue()
    thread_number = 50

    for x in range(1,500):
        que.put(x)

    while not que.empty():
        threads = []

        for x in range(thread_number):
            threads.append(threading.Thread(target=index,args=(que.get(),)))

        for x in threads:
            x.start()

        for x in threads:
            x.join()