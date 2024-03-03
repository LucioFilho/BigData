'''numpy.vectorize is a utility function that transforms a Python function that 
operates on single values into a vectorized function that can operate on arrays. 
While it doesn't improve performance by itself—since it essentially loops over the input 
array elements—it can make your code cleaner and easier to read by allowing you to apply 
custom operations over NumPy arrays in a vectorized manner. However, remember that for 
performance-critical code, using built-in NumPy operations or writing custom NumPy ufuncs 
(universal functions) in C is preferable.'''

## Basic Usage of numpy.vectorize ##
'''Let's start with a simple example where we have a custom function 
that we want to apply to each element of a NumPy array.'''

# Squaring Function
'''Suppose we have a simple function that squares its input. 
e can use numpy.vectorize to apply it over an array.'''
import numpy as np

# Define a simple function
def square(x):
    return x ** 2

# Vectorize the function
vectorized_square = np.vectorize(square)

# Create an array
arr = np.array([1, 2, 3, 4, 5])

# Apply the vectorized function
squared_arr = vectorized_square(arr)
print("Squared array:", squared_arr)

## Applying a Conditional Function ##
'''numpy.vectorize can also be used for functions that involve conditional logic, 
which might be less straightforward to vectorize using NumPy's built-in operations.'''

# Custom Modulo Checker
'''Let's create a function that checks if a number is divisible by 
a given divisor and returns a custom message based on the result.'''
# Define a function with conditional logic
def is_divisible_by(x, divisor=2):
    if x % divisor == 0:
        return f"{x} is divisible by {divisor}"
    else:
        return f"{x} is not divisible by {divisor}"

# Vectorize the function
vectorized_divisible_by = np.vectorize(is_divisible_by)

# Apply the vectorized function with an extra argument
divisible_arr = vectorized_divisible_by(arr, 3)
print(divisible_arr)

## Performance Considerations ##
'''It's important to note that while numpy.vectorize makes it easy to write clean 
and concise code, it does not inherently make code run faster. In fact, it can be 
slower than a well-optimized loop written in pure Python, especially for complex functions. 
The performance overhead comes from the Python function call overhead, which is significant 
compared to the low-level loop executed in compiled NumPy operations.'''

## When to Use numpy.vectorize ##

# Convenience: 
'''When you need to quickly apply a custom function 
over a NumPy array without writing loops explicitly.'''

# Readability: 
'''When using numpy.vectorize makes your code more readable and easier to understand.'''

# Prototyping: 
'''During the initial stages of development when performance is not the primary concern.'''

## Alternatives for Performance ##
'''If you find that using numpy.vectorize becomes a performance bottleneck, 
consider the following alternatives:'''

# Use Built-in NumPy Functions: 
'''Whenever possible, use NumPy's built-in operations and functions, 
as they are optimized for performance.'''

# Write Custom ufuncs: 
'''For performance-critical applications, you can write custom universal functions 
(ufuncs) in C, which can then be used from Python. This requires more effort but can 
significantly improve performance.'''

# Cython or Numba: 
'''Tools like Cython or Numba can compile Python code to C or use JIT (Just-In-Time) compilation, 
respectively, to speed up array operations.'''

'''numpy.vectorize is best viewed as a tool for convenience and code clarity 
rather than a method for improving computational performance.'''
