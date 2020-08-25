from multiprocessing import Process
import time

# 多进程相对于单进程的优势在计算密集型任务上的优势。

def jisuan(times):
    if times == 333:
        exit()
    i = 0
    for x in range(times):
        i += x


def alone_process(times):
    start_time = time.time()

    for x in range(times):
        jisuan(100000000)

    print("单进程启{}个任务，耗时为：{}".format(times,time.time()-start_time))

def multi_process(times):

    process_list = []
    start_time = time.time()
    p1 = Process(target=jisuan,args=(333,))
    p2 = Process(target=jisuan,args=(100000000,))
    p3 = Process(target=jisuan,args=(100000000,))
    p4 = Process(target=jisuan,args=(100000000,))
    p5 = Process(target=jisuan,args=(100000000,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

    for x in range(5):
        Process(target=jisuan,args=(100000000,)).start


    print("多进程起{}个任务，耗时为：{}".format(times,(time.time()-start_time)))




if __name__ == "__main__":

    alone_process(5)
    multi_process(5)
