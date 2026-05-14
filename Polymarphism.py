

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return f'{self.name} makes a sound' 
class Dog(Animal):  
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        return f'{self.name} barks' 
class Cat(Animal):  
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def make_sound(self):
        return f'{self.name} meows' 
class Cow(Animal):      
    def __init__(self, name, species, milk_production):
        super().__init__(name, species)
        self.milk_production = milk_production

    def make_sound(self):
        return f'{self.name} moos'      
    
    print('Polymorphism in Python')  
    layka = Dog('Layka', 'Canine', 'Labrador')      
    print(layka.make_sound())   
    tom = Cat('Tom', 'Feline', 'Gray')  
    print(tom.make_sound())     
    bessy = Cow('Bessy', 'Bovine', 20)   # type: ignore
    print(bessy.make_sound())   