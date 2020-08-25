class Student(object):
    __slots__=('name','age','set_age')#这里使用__slots__仙子此类的实例的属性,这里不添加set_nage的话就不能给实例绑定set_age方法，以至于赋值age属性
s=Student()
def set_age(self,age):
    self.age=age
from types import MethodType#导入MethodType方法
s.set_age=MethodType(set_age,s)#使用MethodType方法，给实例s绑定方法set_age 
s.set_age(88)#s使用set_age方法给s.age属性赋值
#s2=Student()
# print(s2.age(10))这段说明了给实例绑定的方法不能给另一个实例
def set_name(self,name='jiyi'):
    self.name=name
s.name=MethodType(set_name,s)
s.name('adic')
print(s.age)
print(s.name)
Student.set_name=set_name#我试了一试发现不能用MethodType方法给类绑定方法
o=Student()
y=Student()
# y.set_name('jiyi')
y.set_name('see')#这是绑定方法
o.set_name('c')
print(o.name)
print(y.name)#这是调用方法获得的属性


#使用slots
y=Student()
y.name='jav'
print(y.name)
print(hasattr(Student,'set_age'))