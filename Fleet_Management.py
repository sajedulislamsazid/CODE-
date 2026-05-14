class Company: 

    def __init__(self, name, address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []   
        self.counters = []  
        self.tickets = []   
        self.managers = []
        self.supervisors = []       


class Driver:  
    def __init__(self, license, name, age) -> None:  
        self.license = license
        self.name = name    
        self.age = age  
    
    class Counter:  
        def __init__(self, counter_number, location) -> None:
            self.counter_number = counter_number
            self.location = location    

        class Passenger:  
            def __init__(self, name, age, destination) -> None:
                self.name = name
                self.age = age
                self.destination = destination      

            #    class Supervisor:  
            #             pass 

            red_mia = Driver('red_mia', 'Mia', 30)
            print(red_mia.name)
            