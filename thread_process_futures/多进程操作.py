from multiprocessing import Process
import multiprocessing
import threading
import time


# 主进程结束过后，进程如果没有调用join方法，或者设置为守护进程的话。会继续执行

def jisuan():
    print("开始时间为：{}".format(time.ctime()))
    time.sleep(3)
    print("结束时间为：{}".format(time.ctime()))

if __name__ == "__main__":
    p1= Process(target=jisuan,args=())
    # p1.daemon = True # 如果不加deamon属性的话，主进程结束后，子进程并不会结束
    print("cpu的个数为{cpu_count}".format(cpu_count=multiprocessing.cpu_count()))
    p1.start()
    # p1.join() # 如果不加p1.join()函数的话，主进程不会等待子进程结束。加的话，主进程会等待子进程结束再继续执行
    print("end")        

