def decorator(func):
    def wrapper(*args, **kwargs):
        print('decorator begins')
        func(*args, **kwargs)
        print('decorator ends')
    return wrapper

@decorator
def func(func_parameter):
    print(func_parameter)
func = decorator(func)

func('something')
     