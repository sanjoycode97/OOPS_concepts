"""
nheritance is a way to create a new class based on an existing class. The new class (called the child or subclass) inherits properties and behaviors (methods) from the existing class (called the parent or superclass).

This allows for code reuse and helps organize code more efficiently.

"""

#Rule for making relations
#1. constructor
#2.non private attributes
#3.non private methods

class User:
    def __init__(self) -> None:
        self.name='sanjoy'
        self.gender='male'
    def login(self):
        print("has logged into the portal")

class Student(User):
    def enroll(self):
        print("now he is enrolled into the course")

user1=User()
student1=Student()


print(student1.name)
student1.login()
student1.enroll()




