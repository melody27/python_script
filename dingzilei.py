class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student name:%s'%self.name
    __repr__=__str__
s=Student('jack')
print(s)

class Fiber(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.b+self.a
        if self.a>100000:
            raise StopIteration()
        return self.a
    def __getiter__(self,x):
        a,b=1,1
        for n in range(x):
            a,b=b,a+b
        return a 
for x in Fiber():
    print(x)


print('-'*50)
class Lik(object):
    def __init__(self):
        self.name='jack'
    def __getattr__(self,attr):
        if attr=='melody':
            return lambda x=2 :x-1
    def __call__(self):
        return '实例方法的返回为:%s'%self.name
l=Lik()
print(l.name)
print(l.melody())
print(l())
