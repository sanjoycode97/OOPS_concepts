class BankAtm:
    def __init__(self):
        self.pin=''
        self.balance=0
        #print("i want to check my balance")
        #here self keyword will connect the menu method so once we create object it will call menu method of class bankatm
        self.menu()

    def menu(self):
        user_input=input("""
       1.press 1 to create pin
       2.press 2 to change pin
       3. press 3 to check blance
       4.press 4 to withdraw money
       5.press 5 to exit""")
        #here self keyword connecting every methods with the class
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
        elif user_input=='3':
            self.check_balance()
        elif user_input=='4':
            self.withdraw_money()
        else:
            print('exiting from menu')
            
    
    def create_pin(self):
        user_pin=input('enter your pin here: ')
        self.pin=user_pin

        user_balance=int(input('enter your balance: '))
        self.balance=user_balance
        print('pin created successfully')
        self.menu()

    def change_pin(self):
        old_pin=input('enter your old pin: ')
        if old_pin==self.pin:
            new_pin=input('enter the new pin: ')
            self.pin=new_pin
            print("pin is created successfully")
        else:
            print("please enter correct pin")
        self.menu()
    
    def check_balance(self):
        print(f'your current balance is: {self.balance}')
        self.menu()
    
    def withdraw_money(self):
        enter_amount=int(input('enter the amount that you want withdraw: '))
        if enter_amount<=self.balance:
            self.balance=self.balance-enter_amount
            print(f'you have withdrawn {enter_amount} and available balance {self.balance}')
        else:
            print('you dont have sufficient balance')
        self.menu()
    



  

    
obj=BankAtm()

#different id for class and obj
print(id(obj)) 
print(id(BankAtm))