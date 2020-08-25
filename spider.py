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
    t = "http://hotpics.cc/category/milfs-pics/page/%s/" % page
    print("[+] Spider: %s" % t)

    r = requests.get(t, headers=headers)
    
    if r.status_code == 200:
        retList = re.findall(r'http://hotpics.cc/wp-content/uploads/\d{4}/\d{2}/.*?.jpg', r.text)

        for img in retList:
            download(img)


if __name__ == "__main__":
    q = queue.Queue()
    thread_number = 30

    for page in range(2, 51):
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