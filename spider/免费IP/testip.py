import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

import requests
import time
import threading
import queue
import re


# 测试免费IP是否可用
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}

url = "http://114.55.106.242:8080/index.php"
def find_ip(ip):
    print(ip)
    proxies = {
        "http":"{}".format(ip)
    }

    start_time = time.time()
    try:
        r = requests.get(url=url,proxies=proxies,timeout=3)
    except Exception as identifier:
        return
    end_time = time.time()
    print("耗时为：",end_time - start_time)
    if r.text not in ip:
        print("对不上")
        print(r.text)
        return 
    # print(r.text,"and",ip)

    if re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",r.text):
        with open("D:\\cpan\\桌面\\test\\hwtest\\ip\\ipuse.txt","a+",encoding="utf-8")as f:
            f.write(ip + "\n")
            print("此IP可用",r.text)
            return 




if __name__ == "__main__":



    times = 0
    len_times = 50
    q = queue.Queue()

    thread_list = []
    with open("D:\\cpan\\桌面\\test\\hwtest\\ip\\iptxt.txt","r+",encoding="utf-8") as e :
        while True:

            ip = e.readline()
            print(ip)
            if ip :
                times += 1
                q.put(ip.strip())

                if times == len_times:

                    for x in range(len_times):
                        thread_list.append(threading.Thread(target=find_ip,args=(q.get(),)))
                    for y in thread_list:
                        y.start()
                    for x in thread_list:
                        x.join()
                    times = 0
                    thread_list = []
            else :
                break
    



    

    
