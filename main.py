# Written by Gregory Post Davis
# Jan 21, 2023

from Object import Object
from Person import Person


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__': # This determines the "main" file and everything below here only runs on startup (ie not if you make a main.py object)
    print_hi('Gregory')

    obj = Object(5)
    obj.print_value()

    person1 = Person()
    person2 = Person(name = "Steve Adams")
    person3 = Person(age = 60)
    person4 = Person("Greg Smith")

    person1.print_person()
    person2.print_person()
    person3.print_person()
    person4.print_person()

    #print(obj.value)



