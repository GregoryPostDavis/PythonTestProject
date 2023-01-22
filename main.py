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

    #person1.giveObject(5)
    person2.giveObject(obj)
    person3.giveObject(Object("Gloves"))

    person3.print_person()

    if(input("Has your day been good, Yes or No ").lower() == "yes"):
        print("I'm glad your day has been good!")
    else:
        print("I'm sorry your day wasn't good")


    #print(obj.value)
""" this is how you make

a multiline comment"""

"""
you can also do it this way
"""

