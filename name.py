class Student(object):
    age=19
    def __init__(self,name):
        self.name=name
    def ff(self):
        print(Student.age)
class ss(Student):
    pass
dd=ss('akli')

print(dd.name)
print(dd.age)
print('_'*10)
dd.ff()