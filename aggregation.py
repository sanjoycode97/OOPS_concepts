class Patient:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
#private variable of Address not accesible in patient we need to define get method
    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)
        #print(self.address._Address__city,self.address.pin,self.address.state)
        #print(self.address.city,self.address.pin,self.address.state) #when we use private keyword it is not accesible as it will associated with class



class Address:
    def __init__(self,city,pin,state):
        self.__city=city
       # self.__city=city
        self.pin=pin
        self.state=state
    def get_city(self):
        return self.__city
    def set_city(self,new_city):
        self.__city=new_city


add1=Address("kolkata",700039,"westbengal")
cust1=Patient("avik","male",add1)


cust1.print_address()
print("setting the new city name to the address")

#add1.city="mumbai"
add1.set_city("mumbai")

print() 
print("new adress details")
print()
cust1.print_address()

#cust1.address holds a reference to the add1 object, not a copy of it.
#When you do cust1.print_address(), Python follows the reference to the add1 object and prints its attributes.
#cust1.address is a reference to the add1 object.
#Any changes to add1 will reflect in cust1 because they point to the same object.


        
    

    