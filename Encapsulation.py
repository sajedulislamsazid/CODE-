#Encapsulation  ->> > hiding the data and providing access to it through methodsHidden data is called private data and it can be accessed only through methods of the class.            
#Access modifiers are used to define the scope of the variables and methods. There are three types of access modifiers in Python: public, protected and private.            

class Bank:  
    def __init__(self, holder_name, location, established_year,deposit_name):
        self.holder_name = holder_name
        self.location = location
        self.established_year = established_year
        self.deposit_name = deposit_name

    def open_account(self, account_type):
        return f'Opening {account_type} account in {self.holder_name} bank'

    def close_account(self, account_type):
        return f'Closing {account_type} account in {self.holder_name} bank'

class Customer:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def withdraw(self, amount):
        return f'Withdrawing {amount} from {self.name} account'         



    print('Encapsulation in Python')    
    rafsun = Bank('Rafsun', 'Dhaka', 2000, 'Savings')
    print(rafsun.open_account('Savings'))
    rafsun.deposit_name = 'Current'     
    print(rafsun.open_account(rafsun.deposit_name))     



