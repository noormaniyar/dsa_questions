"""
1. Decorators:
A decorator is a function that takes another function (or method) and extends its behavior without explicitly modifying it. 
Decorators are often used to modify or enhance functions dynamically.
"""

# Simple decorator that prints something before and after a function call
def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()  # Call the original function
        print("Something after the function.")
    return wrapper

@my_decorator  # Using the decorator
def say_hello():
    print("Hello!")

# Using the decorated function
say_hello()



def try_decorator(function):
    def wrapper():
        decorator_res = "Decorator Result is: "
        print(decorator_res)
        function()
    return wrapper



@try_decorator
def myname():
    name = 'nooruddin maniyar.'
    print(name)
    
myname()

# try_decorator(myname)()


def make_sum(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper

@make_sum
def calculatethesum(a, b):
    return a + b

result = calculatethesum(4, 4)
print(result)
