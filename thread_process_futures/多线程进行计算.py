import threading
import time

# 多线程在计算密集任务上比单线程的劣势


def jisuan(times):
    i = 0
    for x in range(times):
        i += x
        # print(i)

if __name__ == "__main__":
    print("单线程开始")
    start_time = time.time()
    jisuan(200000000)
    jisuan(200000000)
    print("单线程用时为：{}".format((time.time()-start_time)))

    thread_list = []
    print("多线程开始")
    thread_start_time = time.time()
    for x in range(2):
        thread_list.append(threading.Thread(target=jisuan,args=(200000000,)))
    for x in thread_list:
        x.start()
    for x in thread_list:
        x.join()
    print("多线程耗时为：{}".format(time.time()-thread_start_time))



