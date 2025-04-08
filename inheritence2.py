class Phone:
    def __init__(self,price,brand,camera) -> None:
        print("inside the Phone's constructor")
        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("buying a phone")

class Smartphone(Phone):
    pass


phone1=Smartphone(8000,'samsung',"25mp")
phone1.buy()