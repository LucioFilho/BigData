'''NumPy provides a comprehensive set of functions for performing aggregations and reductions 
on arrays, enabling you to easily compute summary statistics and cumulative values. 
These operations are highly optimized and can be performed with simple, concise syntax.'''

import numpy as np

## Basic Aggregations ##
# Aggregation functions compute a summary statistic about the elements in an array.

# Sum: Total of Elements
arr = np.array([1, 2, 3, 4, 5])
total = np.sum(arr)
print("Sum:", total)

# Max and Min: Finding Extreme Values
max_value = np.max(arr)
min_value = np.min(arr)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

# These functions can also operate along a specific axis in a multi-dimensional array.
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
max_in_rows = np.max(arr_2d, axis=1)  # Max in each row
min_in_columns = np.min(arr_2d, axis=0)  # Min in each column
print("Max in rows:", max_in_rows)
print("Min in columns:", min_in_columns)

## Reductions ##
'''Reductions are operations that process the elements of an array to reduce its dimension 
by one or more dimensions.'''

'''This function returns an array of the same size with each element at index i 
being the sum of elements from index 0 to i.'''

# cumsum: Cumulative Sum
cumulative_sum = np.cumsum(arr)
print("Cumulative sum:", cumulative_sum)

# cumprod: Cumulative Product
cumulative_product = np.cumprod(arr)
print("Cumulative product:", cumulative_product)

# Like cumsum, cumprod computes the cumulative product of elements along a given axis.

## Advanced Aggregations ##
'''NumPy also supports more complex aggregations, like mean, standard deviation, 
and more, which can provide deeper insights into your data.'''

# Mean: Average of Elements
mean_value = np.mean(arr)
print("Mean value:", mean_value)

# std: Standard Deviation
std_dev = np.std(arr)
print("Standard deviation:", std_dev)

# var: Variance
variance = np.var(arr)
print("Variance:", variance)

## Multidimensional Aggregations ##
'''When working with multidimensional arrays, you can specify 
the axis along which to perform the aggregation.'''

# Aggregations on a 2D Array
# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Sum across different axes
sum_rows = np.sum(arr_2d, axis=1)  # Sum of each row
sum_columns = np.sum(arr_2d, axis=0)  # Sum of each column

print("Sum of rows:", sum_rows)
print("Sum of columns:", sum_columns)

## Conclusion ##
'''NumPy's aggregation and reduction functions are powerful tools for summarizing 
and analyzing data stored in arrays. By providing built-in functions for common mathematical 
and statistical operations, NumPy enables efficient and expressive data manipulation, 
making it an indispensable tool for data analysis, scientific computing, and more.'''