'''A decorator is a function that takes another function and extends its behavior 
without explicitly modifying it. It's a powerful tool for adding functionality 
to existing code (such as logging, timing, or access control checks) in a clean, 
readable manner.'''

# Basic Decorator Example
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with Arguments
'''This example shows how to create a decorator that works with functions 
that accept arguments.'''

def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@decorator_with_args
def say_message(message):
    print(message)

say_message("Hello with arguments")

