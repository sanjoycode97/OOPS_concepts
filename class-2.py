class Fraction:
    def __init__(self,x,y):
        self.num=x
        self.den=y
        #magic method
    #def __str__(self) -> str:
    #   return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,other):  #self is obj1 and other will be obj2 and they both gonna be add obj1+obj2
        new_num=self.num*other.den+other.num*self.den
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __sub__(self,other):  #self is obj1 and other will be obj2 and they both gonna be add obj1+obj2
        new_num=self.num*other.den-other.num*self.den
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __mul__(self,other):  #self is obj1 and other will be obj2 and they both gonna be add obj1+obj2
        new_num=self.num*other.num
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*other.num
        return '{}/{}'.format(new_num,new_den)
    
    def to_decimal(self):
        return self.num/self.den
    
    



obj1=Fraction(2,3)
obj2=Fraction(3,4)

print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)
print(obj1/obj2)
print(obj1.to_decimal())



class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    def add(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def subtract(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def multiply(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def divide(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return '{}/{}'.format(new_num, new_den)

# Using the calculator without magic methods
obj1 = Fraction(2, 3)
obj2 = Fraction(3, 4)

print(obj1.add(obj2))  # You must call methods explicitly
print(obj1.subtract(obj2))
print(obj1.multiply(obj2))
print(obj1.divide(obj2))





"""
The error happened because the __add__ method was missing the second argument other, which represents the other object you're adding to self.

You need to define __add__(self, other) so that the method knows about the second fraction you're adding to the first one.

The method now returns a new Fraction object after performing the addition.

"""