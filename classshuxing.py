class Student(object):
    name='student'
print(Student.name)
s=Student()

s.name='jack'
print(s.name)
del s.name
print(s.name)
