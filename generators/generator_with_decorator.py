'''While decorators and generators serve different purposes, 
hey can be used together in advanced scenarios, 
such as creating a decorator that measures the execution time 
of a generator function.'''

# Using Generators with Decorators

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function took {end - start} seconds to run.")
        return result
    return wrapper

@timing_decorator
def my_generator():
    for i in range(5):
        time.sleep(1)
        yield i

for value in my_generator():
    print(value)
