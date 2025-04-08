class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def greet(self):
        print(f"Hello, I'm {self.name} from {self.country}!")

# Creating an instance (reference variable)
sanjoy = Person('Sanjoy', 'India')

# Using the reference to add new attributes
# This is still the same object, just adding new data to it
sanjoy.age = 25
sanjoy.profession = 'Engineer'

# Accessing new attributes via the reference
print(sanjoy.age)         # Output: 25
print(sanjoy.profession)  # Output: Engineer

# Creating another reference to the same object
new_ref = sanjoy

# Adding another attribute using the new reference
new_ref.city = 'Mumbai'

# Both references point to the same object
print(sanjoy.city)  # Output: Mumbai
print(new_ref.city) # Output: Mumbai
