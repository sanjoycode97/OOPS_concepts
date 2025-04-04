class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addition(self):
        return self.num1+self.num2
    
obj1=Calculator(2,3)
print(obj1.addition())

class Calculator1:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __add__(self,other):
        return self.num1+self.num2
    
    
obj2=Calculator1(2,3)
print(obj2+obj2)


class Calculator2:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def __add__(self, other):
        return self.num1 + self.num2+other.num1+other.num2 # Adding the numbers

# Creating an object of Calculator1
obj3 = Calculator2(2, 3)
obj4=Calculator2(4,5)

# Using the + operator, which invokes the __add__ method
print(obj3 + obj4)  # Output: 10 (since 2 + 3 + 2 + 3 = 10)



