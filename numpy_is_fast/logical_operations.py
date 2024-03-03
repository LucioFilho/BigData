import numpy as np
'''Logical and mathematical operations are fundamental in array programming, 
allowing you to perform element-wise comparisons and calculations across arrays efficiently. 
NumPy, with its comprehensive set of functions and operators, excels in this area, 
enabling concise and fast operations.'''

## Logical Operations ##
'''Logical operations on arrays can be used for element-wise comparison, returning a boolean array 
where each element reflects the outcome of the logical operation.'''

# Comparing Array Elements
'''Let's create an array and apply a logical condition 
to find elements that meet a certain criterion.'''

'''In this example, arr > 3 returns a boolean array (mask) where each element's value 
is True if the corresponding element in arr is greater than 3 and False otherwise. 
Using this mask, arr[mask] selects and returns the elements that satisfy the condition.'''

# Creating an array
arr = np.array([1, 2, 3, 4, 5, 6])

# Finding elements greater than 3
mask = arr > 3
print("Mask:", mask)
print("Elements greater than 3:", arr[mask])

## Mathematical Operations ##
'''NumPy supports a wide range of mathematical operations that can be performed on arrays, 
enabling complex calculations with simple syntax.'''

# Element-wise Addition, Subtraction, Multiplication, and Division
# Element-wise addition
add_result = arr + 10
print("Addition:", add_result)

# Element-wise subtraction
subtract_result = arr - 2
print("Subtraction:", subtract_result)

# Element-wise multiplication
multiply_result = arr * 2
print("Multiplication:", multiply_result)

# Element-wise division
division_result = arr / 2
print("Division:", division_result)

# More Complex Mathematical Functions
'''NumPy provides functions for more complex mathematical operations, 
such as exponential and trigonometric functions.'''

# Exponential
exp_result = np.exp(arr)
print("Exponential:", exp_result)

# Square root
sqrt_result = np.sqrt(arr)
print("Square root:", sqrt_result)

# Sine
sin_result = np.sin(arr)
print("Sine:", sin_result)

## Combining Logical and Mathematical Operations ##
'''Logical and mathematical operations can be combined 
to perform more complex queries and calculations.'''

# Conditional Element-wise Operations
'''Suppose you want to increase values greater than 3 by 10 and leave others unchanged.'''

'''np.where(condition, [x, y]) is a versatile function for element-wise operations based on 
a condition. In this case, it checks arr > 3; for True elements, it adds 10 (arr + 10), 
and for False elements, it leaves them unchanged (arr).'''
# Increase elements greater than 3 by 10
modified_arr = np.where(arr > 3, arr + 10, arr)
print("Modified array:", modified_arr)

# Conclusion
'''NumPy's support for logical and mathematical operations allows for efficient and 
expressive data manipulation. By leveraging these capabilities, you can perform a wide range 
of calculations and conditionals on arrays with minimal code, benefiting from NumPy's optimized 
performance for large datasets. This blend of functionality makes NumPy a cornerstone for 
numerical computing in Python.'''



