# def fn(self,name):
#     self.name=name
#     print(self.name)
#     return self.name
# try:
#     Hello=type('Hello',(object),{'hello':fn})
#     h=Hello()
#     print(h.hello('jack'))
#     Kkp=type('Kkp',(object,),{'ouer':fn})

#     kkp=Kkp()
#     print(kkp.ouer('zhang'))
# except Exception as e :
#     logging.exception(e)
#     print(e)

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()