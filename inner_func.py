#function is a first class object in python. we can return function from another function. we can pass function as              


def double_decker():
    def first_floor():
        print('This is the first floor')
    
    def second_floor():
        print('This is the second floor')
    
    return first_floor, second_floor        

#print(double_decker())  # This will return a tuple containing the two inner functions, first_floor and second_floor. The output will be something like: (<function double_decker.<locals>.first_floor at 0x7f8c8c8c8c8>, <function double_decker.<locals>.second_floor at 0x7f8c8c8c8d0>)      
print(double_decker()[0])  # This will return the first inner function, first_floor, from the tuple returned by double_decker. The output will be something like: <function double_decker.<locals>.first_floor at 0x7f8c8c8c8c8>                    
double_decker()[0]()  # This will call the first inner function, first_floor, from the tuple returned by double_decker. The output will be: This is the first floor     
double_decker()[1]()  # This will call the second inner function, second_floor, from the tuple returned by double_decker. The output will be: This is the second floor          


def double_decker():
    def first_floor():
        print('This is the first floor')
    
    def second_floor():
        print('This is the second floor')
    
    def coding():
        print('This is the coding floor')
    
    return first_floor, second_floor, coding        

# This will assign the inner function coding to the variable do_something.
do_something = double_decker()[2]
do_something()  # This will call the inner function coding, which will print: This is the coding floor. The output will be: This is the coding floor        


def sleeping():
    def sleep():
        print('Sleeping...')
    
    return sleep            
sleeping()()  # This will call the sleeping function, which returns the inner function sleep, and then immediately calls the sleep function. The output will be: Sleeping... The output will be: Sleeping...    

def coding():
    def python():
        print('Coding in Python...')

    return python

do_something = coding()  # This will call the coding function, which returns the inner function python, and assigns it to the variable do_something. It does not print anything by itself.




