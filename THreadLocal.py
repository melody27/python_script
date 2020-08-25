#究其原因这个Threadlocal的作用就是使用的多线程时便于在函数见传递参数
    #可以把threadlocal看作是线程的局部变量
class dent(object):
    def __init__(self,name):
        self.name=name
import threading
local_student=threading.local()
def er():
    sth=local_student.dent
    print('Hellow%s,(in %s)'%(sth,threading.current_thread().name))
def yi(name):
    local_student.dent=name
    er()
ti1=threading.Thread(target=yi,name='线程1',args=('jackal',))
ti2=threading.Thread(target=yi,name='线程2',args=('张某',))
ti1.start()
ti2.start()
ti1.join()
ti2.join()