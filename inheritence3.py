class Phone:
    def __init__(self,price,brand,camera) -> None:
        print("inside the Phone's constructor")
        #self.price=price
        self.__price=price #we can't access this attribute because of the private  so it cant build relation with two class
        self.brand=brand
        self.camera=camera

    def show(self):
        #print(self.price)
        print(self.__price)

# inheritance can read parent class constructor here smartphone can read the phone constructor here
#non private attributes in parent class price ,brand,camera
#non private function in the parent class buy so we can make relation
#when we create the child class constructor then machine will only reach to child class consyructor the how to connect parent class we need to use super
        
class Smartphone(Phone):
    def check(self):
        #print(self.price)
        print(self.__price)
        #print(self._Phone__price) accessing private key word


phone1=Smartphone(8000,'samsung',"25mp")
#print(phone1.__price)
phone1.show()
phone1.check()
print(phone1.brand)
print(phone1.camera)


"""
 Private Attributes in Python:
Not accessible outside the class.

Not accessible in child classes, even with inheritance.

Name mangling makes it hard to access, but technically possible with special syntax like self._ClassName__attribute.

"""