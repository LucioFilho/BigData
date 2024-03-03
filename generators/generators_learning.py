'''Generators provide a way to create iterators in a more pythonic manner 
without relying on class-based approaches. They use the yield statement to produce 
a sequence of values lazily, which means generating values only as needed, 
leading to improved performance and lower memory usage.'''

'''This generator function yields values one at a time. 
Iterating over the generator with a for loop prints 1, 2, and 3, 
each value generated lazily.'''

# Basic Generator Example
def my_generator():
    yield 1
    yield 2
    yield 3
'''
gen = my_generator()
for value in gen:
    print(value)
'''

# Generator for Large Sequences
def countdown(num):
    return range(num)

def countit(num):
    for count in countdown(num):
        print(num - count)

countit(5)
