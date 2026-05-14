#@Static attribute(Class attribute) and Static method           
#class method @classmethod      
#difference between static method and class method          



class Shopping:
    cart = []  # This is a class variable, shared by all instances of the Shopping class.
    origin = 'china'

    def __init__(self, name, location):
        self.name = name  # instance variable, unique to each instance.
        self.location = location

    def purchase(self, item, price, amount):
        self.item = item
        self.price = price
        self.amount = amount
        total_price = price * amount
        Shopping.cart.append((item, total_price))
        print(f'{self.name} purchased {amount} {item}(s) for a total of {total_price} dollars.')
        print(f'Current cart: {Shopping.cart}')

    @staticmethod
    def multiply(a, b):
        result = a * b
        print(f'The result of multiplying {a} and {b} is: {result}')
        return result

    @classmethod
    def hudai_dekhite(cls):
        print('hudai dekhi')

   

basundhara =  Shopping('Basundhara', 'Dhaka')       
basundhara.purchase('laptop', 1000, 2)      

#Shopping.cart.append(('phone', 500))  # This will add a tuple containing the item 'phone' and its price 500 to the cart list. Since cart is a class variable, it will be shared among all instances of the Shopping class.             
Shopping.cart.append(('phone', 500))  # This will add a tuple containing the item 'phone' and its price 500 to the cart list. Since cart is a class variable, it will be shared among all instances of the Shopping class.      
Shopping.hudai_dekhite()  # This will call the hudai_dekhite classmethod on the Shopping class, which will print the message 'hudai dekhi'.         
Shopping.multiply(5, 10)  # This will call the multiply method on the Shopping class, passing in the arguments 5 and 10. The method will return the result of multiplying 5 and 10, which is 50. Static Method        


basundhara.multiply(5, 10)  # This will call the multiply method on the basundhara instance, passing in the arguments 5 and 10. The method will return the result of multiplying 5 and 10, which is 50.
