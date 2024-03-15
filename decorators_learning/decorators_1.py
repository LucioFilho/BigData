def func():
    print('Function')

def wrapper(func):
    print('hello')
    func()
    print('bye')

def function_generator():
    def new_function():
        print('New function')
    return new_function

# wrapper(func)
    
new_func = function_generator()

