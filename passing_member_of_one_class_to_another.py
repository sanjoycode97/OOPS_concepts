class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def details(self):
        print("name of student ",self.name)
        print("roll of student ",self.roll)


class User:

    @staticmethod
    def show(s):
        print("accessing name ",s.name)
        print("accessing roll number ",s.roll)

stu=Student("anirban",34)
User.show(stu)