import threading
import time

# 因为农夫的kali实际上全是固态，实际的测试效果反倒是单线程更加快。实际在我自己的windows上进行执行的时候，会发现实际上多线程快一些，不过也快不了多少。
# 按理说大规模的读写的话，应该会更加的节约时间。但是对于固态硬盘来说，并划不着

def some_write(name,times):
    with open('/root/桌面/工具/字典/farmsec字典/{}.txt'.format(name+str(times)),'a+') as f:
        for x in range(999999):
            f.writelines(str(x)+'\n')



def alone(times):
    start_time = time.time()
    for x in range(times):
        some_write('alone',x)
    print("单线程写入的次数为：{times}*999999。耗时为：{live_time}".format(times=times,live_time=(time.time()-start_time)))



def trhead_io(times):
    start_time = time.time()
    thread_list = []
    for x in range(times):
        thread_list.append(threading.Thread(target=some_write,args=('thread',x)))
    for x in thread_list:
        x.start()
    for x in thread_list:
        x.join()


    print("多线程写入的次数为：{times}。耗时为：{alive_time}".format(times=times,alive_time=(time.time()-start_time)))


if __name__ == "__main__":
    # alone(3)
    trhead_io(3)