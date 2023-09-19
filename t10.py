import functools

def _not_divisible(n):
    return lambda x: x % n > 0


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n




def primes():
    yield 2
    it = _odd_iter() # 初始序列(奇数队列)
    while True:

        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列。相当于lambda x:x%3



def log(func):
    @functools.wraps(func)      # 简单可以理解为将wapper的__name__属性进行替换
    def wapper(*arg,**kw):
        print("called :"+func.__name__ + "()")
        return func(*arg,**kw)
    return wapper


@log
def now():
    print("2015-7-10")
    return 

def __private_test():
    print("this is a private test")


class Stu(object):
    
    def __init__(self,name,age):
        self.__name = name                   # __name属性外部不能直接引用
        self.__age = age
        self.__sex__ = 'm'                  # 特殊变量，外部可以使用

    def print_info(self):
        print(self.__name,self.__age)



if __name__ == "__main__":
    # for n in primes():
    #     if n < 1000:
    #         print(n)
    #     else:
    #         break
    
    # now()           # 应该参数类型检查是在预编译阶段做的
    # print(now.__name__)
    # __private_test()

    d1 = Stu("coco",17) 
    d1.print_info()
    print("the sex of d1 is "+d1.__sex__)                   #
    d1.__name__ = "melody"                # 此处 __name__的self.__name__不是同一个属性
    print(d1.__name__)
    d1.print_info()                     # 对于python动态语言，多态的使用只需要有同名方法即可
    print(hasattr(d1,"type"))
    print(setattr(d1,"type","man"))     # 通过setattr这种函数，来进行属性的设置
    print(getattr(d1,"type"))
    print(getattr(d1,"school","cqu"))   # 第三个参数可以返回默认值
    