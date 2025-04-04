class Bank:
    def __init__(self,acc_num,name,balance):
        self.acc_num=acc_num
        self.name=name
        self.balance=balance
    def display(self):
        print(f'acc number {self.acc_num}')
        print(f'acc number {self.name}')
        print(f'acc number {self.balance}')

    def deposite(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount>self.balance:
            print('in sufficient balance')
        else:
            available_balance=self.balance-amount
            self.balance=available_balance

obj=Bank(1234,'sanjoy',1000)
obj.deposite(200)
obj.withdraw(10)
obj.display()
