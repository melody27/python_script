"""
这个文件是继承的继承重写，完成一个简单工厂模式
继承自 operation

operationAdd(n, m).get_result()
operationSub(n, m).get_result()
"""
class operation(object):
    def __init__(self,n,m):
        self.n=n
        self.m=m
    def get_result(self):
        pass
class operationFactory(operation):
    def __init__(self,x,y,z):
        self.n=x
        self.k=y
        self.m=z
    def fanctoryjisuan(self):
        oper = None

        if self.k=='+':
            oper=operationAdd(x,z)
        if self.k=='*':
            oper=operationCheng(x,z)
        if self.k=='-':
            oper = operationSub(x,z)
        if self.k=='/':
            oper = operationChu(x,z)
        return oper
class operationAdd(operation):
    def get_result(self):
        return self.n+self.m
class operationSub(operation):
    def get_result(self):
        return self.n - self.m
class operationCheng(operation):
    def get_result(self):
        return self.n * self.m
class operationChu(operation):
    def get_result(self):
        return float(self.n/self.m)
x=int(input('输入第一个计算的数'))
y=input('需要进行的运算')
z=int(input('进行运算的第二个数'))
fanctory=operationFactory(x,y,z)
# add.get_result()
# sub.get_result()
# cheng.get_result()
# chu.get_result()
print(fanctory.fanctoryjisuan().get_result())
