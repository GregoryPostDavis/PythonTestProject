from Object import Object
class Person:

    o = None



    def __init__(self, name = "John Smith", age = 25):
        if name:
            self.name = name
        if age:
            self.age = age

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.age)

    def print_person(self):
        print(self.name, " " ,self.age)
        if self.o:
            print(self.o.name)

    def giveObject(self, o = None):
        if isinstance(o, Object):
            self.o = o
        else:
            raise TypeError("o must be of type Object")