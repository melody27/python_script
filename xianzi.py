#这个讲了(__name)这种前面加双下划线的访问限制
class Student(object):#这几行主要说了关于给实例的属性改为私有属性
    def __init__(self,name,fen):
        self.__name=name
        self.__fen=fen
    def get__name(self):#获取私有的姓名
        return self.__name
    def get__fen(self):#获取私有的分数
        return self.__fen
    def set__fen(self,fen):#修改私有的分数
        if 0<=fen<=100:
            self__fen=fen
            print(self__fen)
        else :
            return 'sorry'
name=input('姓名')
fen=int(input('分数'))
sam=Student(name,fen)
houfen=int(input('输入你要修改的分数拒绝输入0'))
print(sam.get__name())
print(sam.set__fen(houfen))
#print(sam.name)这里不注释掉的话会报错，报错没有name这个属性
# print(sam.fen)