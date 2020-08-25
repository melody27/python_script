import requests
import threading
import queue
import re


headers={
    'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

def download(img_path):
    r = requests.get(img_path, headers=headers)

    if r.status_code == 200:
        img_save_name = img_path.split("/")[-1]

        with open("imgsave/" + img_save_name, mode='wb') as f:
            f.write(r.content)
            print("%s saved" % img_save_name)

def spider(page):
    t = "http://www.mmonly.cc/tag/br/%s.html" % page#https://www.7160.com/qingchunmeinv/list_2_%s.html
    print("[+] Spider: %s" % t)

    r = requests.get(t, headers=headers)
    
    if r.status_code == 200:
        retList = re.findall(r'http://t1.hxzdhn.com/uploads/tu/\d{6}/\d{1,6}/.*?.jpg', r.text)#https://img.lovebuy99.com/uploads/\d{6}/.*?.jpg

        for img in retList:
            download(img)

# spider(2)
if __name__ == "__main__":
    q = queue.Queue()
    thread_number = 50

    for page in range(2, 100):
        q.put(page)

    
    while not q.empty():
        threads = []

        for i in range(thread_number):
            if not q.empty():
                threads.append(threading.Thread(target=spider, args=(q.get(), )))
        
        for t in threads:
            t.start()
        
        for t in threads:
            t.join()


    # for i in range(2, 6):
    #     threads.append(threading.Thread(target=spider, args=(i, )))
    
    # for t in threads:
    #     t.start()

    # for t in threads:
    #     t.join()