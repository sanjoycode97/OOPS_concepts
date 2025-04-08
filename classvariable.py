#class variable or static variable is variable whose single copy is available for all instances of the class means 
#means if one particular class is having 20 object so we can access that variable nby 20 objects
#if modify class variable for any one instance so it will affect and changed for all other instances

class Vechicle:
    vechicle_is="comuter" #class variable
    def __init__(self,brand,wheel_number):
        self.brand=brand
        self.wheel_number=wheel_number
    
    @classmethod
    def display_details(cls):
        print("class variable O/p is ",cls.vechicle_is) #accessing class variable by class method
        
        

x1=Vechicle("toyota",4)
x2=Vechicle("Hyundai",4)
x3=Vechicle("MArvel",4)
x4=Vechicle("petercar",4)

print("before modifying class variable")
print("*"*30)
print(x1.vechicle_is)
x1.display_details()
print("*"*30)

x3.vechicle_is='bus'
print("modeification done on x3 object lets check for other if it is changed or not")
print("x1",x1.vechicle_is)
print("x2",x2.vechicle_is)
print("x3",x3.vechicle_is)
print("x4",x4.vechicle_is)


print("x1",Vechicle.vechicle_is)
print("x2",Vechicle.vechicle_is)
print("x3",Vechicle.vechicle_is)
print("x4",Vechicle.vechicle_is)

print("modify by class ")
Vechicle.vechicle_is="Bus"

print("x1",Vechicle.vechicle_is)
print("x2",Vechicle.vechicle_is)
print("x3",Vechicle.vechicle_is)
print("x4",Vechicle.vechicle_is)
