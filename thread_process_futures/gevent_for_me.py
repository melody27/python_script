import gevent.monkey            # 必须在程序的最前面导入gevent的monkey包。否则会出现，超出最大递归数的报错
gevent.monkey.patch_all()
import gevent
import requests
import time
from datetime import datetime
import os

# 暂时的社区对asyncio的支持还不够好，所以推荐先使用gevent，gevent方便入手



url_1 = 'https://i0.hdslb.com/bfs/album/214134e4719ca58a420f0637b614e1b1e61f4064.jpg'
url_2 = 'http://www.melodyspace.cn/'

def gevent_requests(url):
    # print("before gevent is ",url)
    r = requests.get(url=url)
    # print("after gevent is ",url)


if __name__ == "__main__":
    
    gevent_start_time = time.time()
    gevent_list= []
    for x in range(99):
        gevent_list.append(gevent.spawn(gevent_requests,url_1+str(x)))

    gevent.joinall(gevent_list)

    print("gevent time is ：{}".format((time.time()-gevent_start_time)))


    # exit()
    thread_start_time = time.time()
    for x in range(99):
        gevent_requests(url_1)
    print("\n\n\n\n\nthread time is ：{}".format((time.time()-thread_start_time)))