class Gadget:
      def __init__(self,brand, price,color):
            self.brand = brand
            self.price = price
            self.color = color
            self.origin = origin     # type: ignore

      def run(self):
            return f'Running laptop:{self.brand}'


class Laptop:  
    def __init__(self, memory, ssd) -> None:
        # self.brand = brand
        # self.price = price
        # self.color = color
        self.memory = memory               
        self.ssd = ssd      
        

    # def run(self):  
    #     return f'phone is running'

    def coding(self):
        return f'learning python'

class Phone:
    def __init__(self, brand, number, dual_sim):
        self.brand = brand
        self.number = number
        self.dual_sim = dual_sim

    def phone_call(self, number):
        return f'Calling to:{number} with {self.brand} and dual sim: {self.dual_sim}'

    def send_sms(self, number, text):   
        return f'Sending SMS to:{number} with {text}'


class Camera:  
    def __init__(self, pixel):
        self.pixel = pixel       
        # self.color = color  
        # self.brand = brand  
        # self.pixel = pixel  

    def run(self):           
        pass

    def change_lens(self):
        pass 