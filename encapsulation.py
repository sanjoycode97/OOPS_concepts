#encapsulation so that we can bind the code in 

class Car:
    def __init__(self,make,model,year):
        self.__make=make
        self.__model=model
        self.__year=year
        self.__mileage=0
    def drive(self,miles):
        self.__mileage = self.__mileage + miles
    def get_mileage(self):
        return self.__mileage
    def  get_info(self):
        return f'company: {self.__make}, model: {self.__model}, year: {self.__year}'
    

my_car=Car('toyota','corolla',2019)
my_car.drive(100)
print(my_car.get_info())
print(my_car.get_mileage())

#here attribute cant be change as it is private attribute no impact on object's attribute name will not change
my_car.__make="hyundai"
print(my_car.get_info())

#if we need to change the attribute even if the private attribute we have to have the class reference
my_car._Car__make="abcd" #permanent change _classname(car)__attributename(make)
print(my_car.get_info())