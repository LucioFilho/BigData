import timeit
import numpy

t = 100_000_000

# sum the numbers from 0 to n - 1 in different ways.

def while_loop(n = t):
    i = 0
    s = 0
    while i < n:
        s += i
        i += 1
    return s

def for_loop(n = t):
    s = 0
    for i in range(n):
        s += i
    return s

def for_loop_with_test(n = t):
    s = 0
    for i in range(n):
        if i < n: pass
        s += i
    return s

def for_loop_with_increment(n = t):
    s = 0
    for i in range(n):
        s += i
        i += 1
    return s

def for_loop_with_increment_and_test(n = t):
    s = 0
    for i in range(n):
        if i < n: pass
        i += 1
        s += i
    return s

def sum_range(n = t):
    return sum(range(n))

def sum_numpy(n = t):
    return numpy.sum(numpy.arange(n))


def sum_math(n = t):
    return (n * (n - 1)) // 2

def main():
    print('while loop\t\t', timeit.timeit(while_loop, number = 1))
    print('for pure\t\t', timeit.timeit(for_loop, number = 1))
    print('for inc\t\t\t', timeit.timeit(for_loop_with_increment, number = 1))
    print('for test\t\t', timeit.timeit(for_loop_with_increment_and_test, number = 1))
    print('sum range\t\t', timeit.timeit(sum_range, number = 1))
    print('numpy sum\t\t', timeit.timeit(sum_numpy, number = 1))
    print('math sum\t\t', timeit.timeit(sum_math, number = 1))


if __name__ == '__main__':
    main()
