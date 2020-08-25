import os
import multiprocessing
import time
def jisuan(a,b):
    for x in range(30):
        print(a,b)
        time.sleep(0.1)
    print('这里是os.getpid数据',os.getpid())
if __name__=='__main__':
    j=multiprocessing.Process(target=jisuan,args=('进程一',0))
    k=multiprocessing.Process(target=jisuan,args=('进程二',1))

    j.start()
    k.start()

    j.join()
    k.join()
    print('j,k进程都执行完毕')

    j.close()
    k.close()