from multiprocessing import Pool
import os,random,time
def chi(name):
    print('传进来的name为%s,getpid值为%s'%(name,os.getpid))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('name为%s,用的时间为%s'%(name,(end-start)))
if __name__=='__main__':
    print('开始游戏,getpid值为',os.getpid())
    p=Pool(4)
    for x in range(5):
        p.apply_async(chi,args=(x,))
    print('现在正式开始进行计算')
    p.close()
    p.join()
    print('计算已经结束')