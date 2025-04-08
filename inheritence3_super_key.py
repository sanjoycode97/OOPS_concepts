class Parent:
    def __init__(self,num):
        self.num=num

    def show_num(self):
        return self.num
    

class Child(Parent):
    def show_details(self):
        print("here is from child class")

son=Child(100)
print(son.show_num())
son.show_details() 