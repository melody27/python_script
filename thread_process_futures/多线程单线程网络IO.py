import threading
import hashlib
import sys
import os
import time
import requests
import queue
import os


# 多线程比单线程在网络IO上的优势


def jisuan():
    r = requests.get('http://192.168.2.119:8000/')
        


def thread(thread_times):
    start_time = time.time()

    thread_list = []
    for x in range(thread_times):
        thread_list.append(threading.Thread(target=jisuan,))
    for x in thread_list:
        x.start()
    for x in thread_list:
        x.join()
    print("耗时：{time}".format(time=(time.time()-start_time)))

def alone_thread(times):

    start_time = time.time()
    for x in range(times):
        jisuan()

    print("线程名：{name},耗时：{time}".format(name=os.getpid(),time=(time.time()-start_time)))

if __name__ == "__main__":

    # 单线程进行执行
    alone_thread(999)
    # 多线程执行
    thread(999)
