import numpy as np

# Using sum: Sum of Elements
# The sum function calculates the sum of array elements over a given axis.

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Calculate sum of all elements in the array
total_sum = np.sum(arr)
print("Sum:", total_sum)

# For multi-dimensional arrays, you can sum over different axes:
# Create a 2D NumPy array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Calculate sum over all elements
total_sum_2d = np.sum(arr_2d)
print("Total Sum:", total_sum_2d)

# Calculate sum over each column (axis 0)
column_sum = np.sum(arr_2d, axis=0)
print("Column-wise Sum:", column_sum)

# Calculate sum over each row (axis 1)
row_sum = np.sum(arr_2d, axis=1)
print("Row-wise Sum:", row_sum)

# Using mean: Average of Elements
# The mean function computes the arithmetic mean along the specified axis.
# Calculate mean of all elements in the array
mean_val = np.mean(arr)
print("Mean:", mean_val)

# Similarly, for multi-dimensional arrays:
# Calculate mean across different axes
column_mean = np.mean(arr_2d, axis=0)
row_mean = np.mean(arr_2d, axis=1)

print("Column-wise Mean:", column_mean)
print("Row-wise Mean:", row_mean)

# Using std: Standard Deviation
# The std function computes the standard deviation, a measure of the dispersion 
# of a set of values, along the specified axis.
# Calculate standard deviation of all elements in the array
std_val = np.std(arr)
print("Standard Deviation:", std_val)

# And for multi-dimensional arrays:
# Calculate standard deviation across different axes
column_std = np.std(arr_2d, axis=0)
row_std = np.std(arr_2d, axis=1)

print("Column-wise Standard Deviation:", column_std)
print("Row-wise Standard Deviation:", row_std)

# Performance Benefits
'''Using NumPy's built-in functions like sum, mean, and std offers significant performance advantages 
over equivalent Python code, especially for large arrays. NumPy operations are vectorized, 
meaning they're efficiently implemented in C and avoid explicit loops in Python. 
This results in faster computation and the ability to work with large datasets that wouldn't be 
feasible with pure Python due to memory and time constraints.'''

# Conclusion
'''Leveraging NumPy's array operations can greatly simplify numerical computations while improving 
performance. By avoiding explicit loops and using these built-in functions, you can write cleaner, 
more efficient code for a wide range of mathematical and scientific applications.'''

