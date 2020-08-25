import time,threading
def fff():
    print('函数第一句',threading.current_thread().name)
    n=0
    while n<5:
        print('函数内的循环',threading.current_thread().name,n)
        time.sleep(1)
        n=n+1
    print('函数循环后的语句',threading.current_thread().name)
print('主函数的语句',threading.current_thread().name)
t=threading.Thread(target=fff,name='子线程')
t.start()
t.join()
print('主函数的最后一句输出语句',threading.current_thread().name)