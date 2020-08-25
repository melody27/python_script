class Person(object):

    def __init__(self):
        self.name2 = "name2"
        self.age = 10

    @property
    def name(self):
        if self.age > 10:
            return "大于10"
        return "不大于10"

    @name.setter
    def name(self, val):
        self.name2 = "通过name setter 设置的值: " + str(val)


if __name__ == "__main__":
    a = Person()
    a.name = "啦啦啦"
    print(a.name2)