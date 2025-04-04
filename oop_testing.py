class Dog:
    var='hello'

    def hellow(self): 
    #def hellow(): self is missing
        print('my bad')
        print(self.var)
obj=Dog()

obj.hellow()

#once we object is created for any particular class and we need to communicate some method or accessing any variable 
#we need mention self variable to communicate with object so self variable will be the reference to that object
#so that object can access those particular attributes or methods associated with that class



