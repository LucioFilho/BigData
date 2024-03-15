import numpy as np
import timeit

i = 1_000_000

# Using traditional for loop
def traditional_for():
    squares = []
    for x in range(i):
        squares.append(x**2)
    return squares

# Using map with lambda
def map_lambda():
    return list(map(lambda x: x**2, range(i)))

# Using list comprehension
def list_comprehension():
    return [x**2 for x in range(i)]

# Using numpy
def numpy_square():
    return np.square(np.arange(i)).tolist()

# Time the different functions
print("Timing traditional for loop:")
print(timeit.timeit(traditional_for, number=1))

print("Timing map with lambda:")
print(timeit.timeit(map_lambda, number=1))

print("Timing list comprehension:")
print(timeit.timeit(list_comprehension, number=1))

print("Timing numpy:")
print(timeit.timeit(numpy_square, number=1))
