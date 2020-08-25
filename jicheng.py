class Animal(object):
        def run(self):
            print('animal is running……')
class Dog(Animal):
        def run(self):
                print('dog is run ……')
class Jack(Dog):
        pass
d=Dog()
j=Jack()
d.run()
j.run()
print(isinstance(d,Dog))
print(isinstance(j,Animal))