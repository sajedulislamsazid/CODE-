class Animal:

    pass

class Dog(Animal):      
    pass        

class Tiger(Animal):  
    pass        

print(issubclass(Dog, Animal))  # This will return True, because Dog is a subclass of Animal. The output will be: True      
print(issubclass(Tiger, Animal))  # This will return True, because Tiger is a subclass of Animal. The output will be: True      
print(isinstance(Dog(), Animal))  # This will return True, because an instance of Dog is also an instance of Animal. The output will be: True       

