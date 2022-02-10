# This file is to demonstrat how class, object and self parameter works in Python.

class Student(object):
#     the init method defines the features of a instance when it is created,
#     the "self" parameter means the instance itself
#     if the brackets only contains "self", when this method is called, the brackets
#     will be left empty.
#     For example in the expression jim.printName(), jim is the self.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = age - 7

    def printGrade(self):
        print(self.grade)
        
    def printName(self):
        print(self.name)

jim = Student("Jim Green",15)
jim.printName()
jim.printGrade()
