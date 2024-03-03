def using_filter_and_map_instead_of_comprehensions():
    xs = list(range(10))
    odds = filter(lambda x: x % 2 == 1, xs)
    squares = map(lambda x: x * x, xs)

    odds = (x for x in xs if x % 2 == 1)
    squares = (x * x for x in xs)

    def func(x):
        ...

    filtered = filter(func, xs)
    filtered = (x for x in xs if func(x))

    mapped = map(func, xs)
    mapped = (func(x) for x in xs)

    filtered = list(filter(func, xs))
    filtered = [x for x in xs if func(x)]

    mapped = list(map(func, xs))
    mapped = [func(x) for x in xs]
