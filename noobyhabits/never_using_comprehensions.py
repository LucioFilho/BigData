def never_using_comprehensions():
    squares = {}
    for i in range(10):
        squares[i] = i * i

# do it instead
def never_using_comprehensions():
    odd_squares = {i: i * i for i in range(10)}

def never_using_comprehensions():
    dict_comp = {i: i * i for i in range(10)}
    list_comp = [x * x for x in range(10)]
    set_comp = {i % 3 for i in range(10)}
    gen_comp = (2 * x + 5 for x in range(10))
