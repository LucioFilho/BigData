'''Applying operations to whole arrays is one of the core strengths of NumPy, 
making it highly efficient for numerical computations. 
This process, known as vectorization, allows you to perform operations on entire arrays 
at once without the need for explicit Python loops. 
'''
# Basic Arithmetic Operations
'''You can perform basic arithmetic operations such as addition, subtraction, 
multiplication, and division on entire arrays with a single operation.'''

import numpy as np

# Addition
# Adding a constant value to each element in an array:
arr = np.array([1, 2, 3, 4, 5])
arr_plus_ten = arr + 10
print("Original array:", arr)
print("After adding 10:", arr_plus_ten)

# Subtraction
# Subtracting a constant value from each element:
arr_minus_two = arr - 2
print("After subtracting 2:", arr_minus_two)

# Multiplication
# Multiplying each element by a constant value:
arr_times_three = arr * 3
print("After multiplying by 3:", arr_times_three)

# Division
# Dividing each element by a constant value:
arr_divided_by_five = arr / 5
print("After dividing by 5:", arr_divided_by_five)

## Applying Functions to Arrays ##
# You can also apply mathematical functions to each element in an array.

#Squaring Each Element
squared_arr = arr ** 2
print("Squared array:", squared_arr)

# Taking the Square Root
sqrt_arr = np.sqrt(arr)
print("Square root of array:", sqrt_arr)

# Logarithm of Each Element
log_arr = np.log(arr)
print("Natural logarithm of array:", log_arr)

# Operations Between Arrays
# Operations can also be applied between arrays element-wise.

# Adding Two Arrays
arr2 = np.array([5, 4, 3, 2, 1])
sum_arrays = arr + arr2
print("Sum of two arrays:", sum_arrays)

# Element-wise Multiplication
product_arrays = arr * arr2
print("Element-wise product of two arrays:", product_arrays)

## Logical Operations ##
# NumPy allows you to perform logical operations on arrays, 
# which can be useful for filtering or conditional operations.

# Greater Than Operation
# This produces a boolean array indicating which elements satisfy the condition.
greater_than_three = arr > 3
print("Elements greater than 3:", greater_than_three)

# Conclusion
'''Applying operations to whole arrays with NumPy is not only concise but also computationally 
efficient, as these operations are optimized and run at C-level speed behind the scenes. 
This makes tasks that involve numerical data manipulation much faster and easier than traditional 
Python loops, particularly with large datasets.'''