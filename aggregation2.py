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
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.edit_address(new_city,new_pin,new_state)



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

    def edit_address(self,new_city,new_pin,new_state):
        self.__city=new_city
        self.pin=new_pin
        self.state=new_state


add1=Address("kolkata",700039,"westbengal")
cust1=Patient("avik","male",add1)

print("before chnaging the address")
print("*"*120)
cust1.print_address()
print("after changing the details")
print("*"*120)
cust1.edit_profile("sanjoy","gurgaon",560005,"Delhi")
cust1.print_address()


#cust1.address holds a reference to the add1 object, not a copy of it.
#When you do cust1.print_address(), Python follows the reference to the add1 object and prints its attributes.
#cust1.address is a reference to the add1 object.
#Any changes to add1 will reflect in cust1 because they point to the same object.


"""
When you call cust1.edit_profile(), it's a method of the Patient class. However, 
inside that method, you’re calling self.address.edit_profile(), 
which delegates the task to the Address object that cust1.address refers to.

cust1.edit_profile("Arjun", "Delhi", 110001, "Delhi")

This is a method of the Patient class.

Inside edit_profile (in Patient class):

Here, self.address is referencing the same Address object (add1).

So, you're calling the edit_profile method of the Address class.

Inside edit_profile (in Address class):

This method updates the __city, pin, and state of the add1 object (which is also cust1.address).

Since both cust1.address and add1 point to the same object, the changes reflect in cust1 as well.


Both objects are linked.

Changes in the Address reflect in the Patient because they are referencing the same object.


cust1  ------------------->  add1 (Address object)
   |                             |
 Patient object               Address object
   |                             |
edit_profile()               edit_profile()  ---> updates __city, pin, state







edit_profile in the Patient class is a method of the Patient object.

Inside it, you're calling another edit_profile method, but of the Address object.

This is called method delegation — where one method delegates work to another.







"""


        
    

    