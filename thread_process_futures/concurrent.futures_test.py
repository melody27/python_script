from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,as_completed,wait
from concurrent import futures
import time
import requests

# 官方文档：https://docs.python.org/zh-cn/3.8/library/concurrent.futures.html#module-concurrent.futures

urls = ['http://www.tencent.com','http://www.google.com/','http://www.kugou.com/']

def jisuan_b(num):
    print("b_time is ：{}。that you num is {}\n".format(time.time(),num))
    return "this is return "

def get_for_content(res):
    r = requests.get(url=res)
    # print(r.text)
    return res

with futures.ThreadPoolExecutor(max_workers=1) as f :
    start_time = time.time()
    # res = f.submit(jisuan_b,'1')          # submit()方法的返回值为一个future对象。此对象可以调用result()方法获取返回值，
    # print(res.result())                 # result函数，实际返回的是回调函数的返回值。result方法本身是阻塞的

    thread_list = []
    for x in urls:
        thread_list.append(f.submit(get_for_content,x))
    # print(wait(thread_list,return_when=FIRST_COMPLETED))              # wait 函数的作用是使主线程阻塞。使满足设定的时候再进行正常执行。
                                            # wait 有三个状态：FIRST_COMPLETED，FIRST_EXCEPTION，ALL_COMPLETED
                                                # FIRST_COMPLETED：只要有一个完成的任务(线程)，就直接的返回，不再进行阻塞。
                                                # FIRST_EXCEPTION：当发生第一个异常的时候退出。如果没有异常的话，就相当于ALL_COMPLETED
                                                # ALL_COMPLETED：当所有的任务(线程)完成的时候退出

    print("执行结束")


    # for x in as_completed(thread_list):     # as_completed函数的作用是接收：executor返回的future对象列表。
                                                # 实际为执行完成的线程返回的furure对象，也就是说安装线程完成的顺序一个一个进行迭代
                                                
    #     print("请求的链接为",x.result())     # 然后使主线程阻塞，如果thread_list中有执行完成的线程的话。会yeid这个线程的result对象。直到所有的线程都执行结束为止
    #                                         # 先完成的线程会先通知主线程。(ps.第二个参数为timeout)
    # print("耗时为：{}".format(time.time()-start_time))


