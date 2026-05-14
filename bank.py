class Bank:  
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'fokira. you can\'t withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f"bank fokir hoye jabo. you can't withdraw more than {self.max_withdraw}")
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')
            print(f'your balance after withdraw: {self.balance}')


brac = Bank(15000)
brac.withdraw(26)
brac.withdraw(5000000)

