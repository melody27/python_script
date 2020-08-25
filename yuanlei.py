def zz(self,name='jack'):
    print('Hello, %s.' % name)
Zhang=type("Zhang",(object,),{'age':55,'xiaozhang':zz})#使用type函数动态创建class
h=Zhang()
print(h.age)
print(h.xiaozhang())
print(type(Zhang))
print(type(h))


