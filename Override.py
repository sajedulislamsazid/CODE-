#Overriding is a feature of OOP that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. The method in the subclass overrides the method in the superclass, allowing the subclass to provide its own behavior while still maintaining the same method signature.


class Person:  

    def __init__(self,name,age,height,weight) ->None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):    
        print('Vegetables')

    def exercise(self):
        print('gym e poisa diya hudai gham jhhoraii')   

    def __add__(self, other):
        return self.age + other.age        


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        super().__init__(name, age, height, weight)
        self.team = team

    def eat(self):
        print('vat mangso polau korma')

    # + sign operator overload
    def __add__(self, other):
        return self.age + other.age

    # * sign operator overload
    def __mul__(self, other):
        return self.age * other.age

    # len overload
    def __len__(self):
        return len(self.name)

    # > operator overload
    def __gt__(self, other):
        return self.age > other.age


sakib  = Cricketer('sakib', 35, 5.9, 75, 'Bangladesh')      
musi   = Cricketer('musi', 30, 5.7, 70, 'Bangladesh')       

# sakib.eat() 
# sakib.exercise()    


#Plus Sign Overload  
print(45+64)
print('Sakib' + 'Rakib')
print([12,98] + [45,67])
print(sakib + musi)  # This will call the __add__ method defined in the Cricketer class, which adds the ages of sakib and musi.     
print(sakib * musi)  # This will call the __mul__ method defined in the Cricketer class, which multiplies the ages of sakib and musi.       
print(len(sakib))  # This will call the __len__ method defined in the Cricketer class, which returns the length of sakib's name.            
print(sakib > musi)  # This will call the __gt__ method defined in the Cricketer class, which compares the ages of sakib and musi and returns True if sakib is older than musi, otherwise it returns False.     



