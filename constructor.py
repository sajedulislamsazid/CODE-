


class phone:
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

class Phone:  
    manufactured = 'China'
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    my_phone = phone('Sneha','Iphone',1200000)
    print(my_phone.owner,my_phone.brand,my_phone.price)
    
    her_phone = phone('Ami Tomar Jan', 'Iphone 14', 900000)
    print(her_phone.owner, her_phone.brand, her_phone.price)

    dad_phone = phone('abbu','Nokia',3000)
    print(dad_phone.owner,dad_phone.brand,dad_phone.price)
    
    