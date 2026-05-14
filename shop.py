class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

mehezbeen = Shop('meh jabeen')
mehezbeen.add_to_cart('shoes')
mehezbeen.add_to_cart('phone')
print(mehezbeen.cart)

nisho = Shop('noisho')
nisho.add_to_cart('cpp')
nisho.add_to_cart('watch')
print(nisho.cart)


          