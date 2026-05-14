class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            print(item)
            total += item['price'] * item['quantity']
        print('total price', total)
        if amount < total:
            print(f'Please Provide {total - amount} more')

swapan = Shopping('Alan Swapon')
swapan.add_to_cart('alu', 50, 6)
swapan.add_to_cart('dim', 12, 24)
swapan.add_to_cart('rice', 50, 5)

swapan.checkout(500)    
swapan.checkout(1000)   
swapan.checkout (2000)

