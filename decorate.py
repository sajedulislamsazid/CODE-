def timer(func):
    def wrapper():
        print('Function is being called')
        func()
        print('Function has been called')
    return wrapper      
@timer
def say_hello():            
    print('Hello, World!')  
say_hello()  # This will call the say_hello function, which has been decorated with the timer decorator. The output will be: Function is being called Hello, World! Function has been called    




