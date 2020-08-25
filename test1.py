class Student(object):
    def __init__(self,age):
        self.age=age
    def get_age(self):
        print(2)
f={Student(7),Student(9)}
for x in f:
    print(x.age,x.get_age())