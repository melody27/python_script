from multiprocessing import Process,Queue
import random,time,os
def write(q):
    print('writh里的getpid值为',os.getpid())
    for x in ['a','b','c']:
        print('写入的值为',x)
        q.put(x)
        time.sleep(random.random())
def read(q):
    print('read里的getpid值为',os.getpid())
    while True:
        value=q.get(True)
        print('read里获取到的值为',value)
if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()