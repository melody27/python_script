#这个py文件讲类和实例
class Student(object):
    def __init__(self,name,fen):
        self.name=name
        self.fen=fen
    def print_score(self):#直接打印出
        print('%s: %s' % (self.name, self.fen))
    def print_fen(self):
        if self.fen>90:
            return 'a'
        elif self.fen>60:
            return 'b'
        else :
            return  'c'
name=input('姓名')
fen=int(input('分数'))
sam=Student(name,fen)
# print(name.name)
# print(name.fen)
print(sam.print_score())
print(sam.print_fen())
