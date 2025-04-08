#reference variable

class Person:
    #species = 'Homo Sapiens' this is class attribute
    def __init__(self,name_input,country_input):
        self.name=name_input  #instance /attribute  # Instance variable (holds data for each object)
        self.country=country_input  #instance / attribute

    def greet(self): #functions
        if self.country=='india':
            print('namastey ',self.name)
        else:
            print('hello everyone')

#sanjoy is the refrence variable pointing towards the person object
sanjoy=Person('sanjoy','india')
print(sanjoy.name)

#creating attribute or instance outside of the class explicitly

sanjoy.gender='male'

#reference is nothing its a variable hold the object(without touching class we are adding new instance or attributes)
#You can also add attributes dynamically to instances outside the class:
print(sanjoy.gender)


"""
sanjoy is a reference to a Person object.

The object itself is stored in memory, and sanjoy points to it.

Python allows dynamic attributes because of its flexible object model.
we can create object without an refrence variable



---------------------------------------------------------

Now, both sanjoy and arya are reference variables pointing to the same object in memory.

You can modify the object through either reference.

"""

print()
print('-'*120)
print()


class Dog:
    def __init__(self):
        self.dog_sound='bark'
        self.dog_gender='male'

lab=Dog()
spitz=lab

print('both id same because its reference to same Object/class dog')
print(id(lab))
print(id(spitz))
print()
print('both will give same property')
print()
print(lab.dog_sound)
print(spitz.dog_sound)
spitz.dog_sound='Bow bow'
print()
print('sound changed')
print()
print(lab.dog_sound)
print(spitz.dog_sound)



        
        