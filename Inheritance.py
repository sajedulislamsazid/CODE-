class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin    
    
    def run(self):
        return f'Running laptop:{self.brand}'


class Laptop:  
    def __init__(self, memory, ssd) -> None:
        self.memory = memory              
        self.ssd = ssd      
    
    def coding(self):
        return f'learning python'


class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim):
        super().__init__(brand, price, color, origin)
        self.dual_sim = dual_sim

    def phone_call(self, number):
        return f'Calling to:{number} with {self.brand} and {self.dual_sim}'
    def send_sms(self, number, text):   
        return f'Sending SMS to:{number} with {text}'


class Camera:  
    def __init__(self, pixel):
        self.pixel = pixel       
    
    def run(self):           
        pass
    
    def change_lens(self):
        pass 

#inheritance  

my_phone = Phone(True)
my_phone.phone_call()
my_phone.brand
my_phone.send_sms()


print(my_phone)



    
   