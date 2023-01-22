class Person:

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