
class Vehicle:

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def move(self):
        pass


class Car(Vehicle):

    def __init__(self, name, price, brand) -> None:
        super().__init__(name, price)
        self.brand = brand

    def move(self):
        return f'{self.name} is moving'


class Truck(Vehicle):

    def __init__(self, name, price, capacity) -> None:
        super().__init__(name, price)
        self.capacity = capacity

    def move(self):
        return f'{self.name} is moving with a capacity of {self.capacity} tons'


class PickupTruck(Truck):

    def __init__(self, name, price, capacity, off_road_capability) -> None:
        super().__init__(name, price, capacity)
        self.off_road_capability = off_road_capability

    def move(self):
        return f'{self.name} is moving with a capacity of {self.capacity} tons and off-road capability: {self.off_road_capability}'


class ACBus(Vehicle):

    def __init__(self, name, price, seating_capacity) -> None:
        super().__init__(name, price)
        self.seating_capacity = seating_capacity

    def move(self):
        return f'{self.name} is moving with a seating capacity of {self.seating_capacity} passengers'
    
    
       