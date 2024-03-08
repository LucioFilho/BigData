'''A happy number is defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares 
of its digits, and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. Those numbers for which 
this process ends in 1 are happy numbers.

To determine whether a number is happy, you can implement a function that follows 
this process. It's common to use a set to keep track of numbers that have already 
been seen to detect loops. Here's a Python function that implements this algorithm:'''

def is_happy(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
        
        if n == 1:
            return True
    
    return False

# Example usage:
n = 19
print(f"Is {n} a happy number? {is_happy(n)}")
