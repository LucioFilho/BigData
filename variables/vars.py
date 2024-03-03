# media = 0
# my_var_name = 'Lúcio Filho'
# n1 = n2 = n3 = 0.0
# a, b, c = 10, 'Sun', 2
# my_status = True

# # type() Function
# print(f'Type media: {type(media)}')
# print(f'Type my_var_name: {type(my_var_name)}')
# print(f'Type n1: {type(n1)}')
# print(f'Type a: {type(a)}')
# print(f'Type my_status: {type(my_status)}')
# print(f'Type complex: {type(1+2j)}')

# # isinstance() Function
# print(isinstance(a, int))

# # Define the limit for the Fibonacci sequence
# n = 10  # For example, generate the first 10 Fibonacci numbers

# # Initialize the first two numbers of the Fibonacci sequence
# a, b = 0, 1
# count = 0
# # Initialize the list to store Fibonacci sequence
# fibonacci = []

# # Loop to generate the Fibonacci sequence up to n numbers
# while count < n:
#     print(a, end=' ')  # Print the current Fibonacci number
#     fibonacci.append(a)  # Add the current Fibonacci number to the list
#     # Update the values of a and b to the next two numbers in the sequence
#     a, b = b, a + b
#     count += 1  # Increment the counter

# # At this point, 'a' and 'b' have the values of the next two Fibonacci numbers after the first 'n' numbers
# # If you want to add these to the fibonacci list as well:
# fibonacci.append(a)
# fibonacci.append(b)

# # fibonacci now contains the first 'n' Fibonacci numbers, plus the next two values in the sequence
# print("\nFibonacci sequence:", fibonacci)

# XP
#x_power = 0.1
# x_time = 307584000 #1 year in seconds
# xp = 0
# count = 1

# while count < x_time:
#     xp += count**x_power
#     count += 1

#print (6)

# números primos hard way to do it

# def es_primo(num):
#     for i in range(2,num-1):
#         if num%i==0: return False
#     return True

# def primos_hasta(num):
#     primos = []
#     for i in range(3,num+1):
#         resultado = es_primo(i)
#         if resultado == True: primos.append(i)
#     return primos

#resultado = primos_hasta(98)
#print(resultado)

#números primos short way to do it
# def es_primo(num):
#     return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

# def primos_hasta(num):
#     return [i for i in range(2, num + 1) if es_primo(i)]

# resultado = primos_hasta(98)
# print(resultado)

#primos
#primos_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))
#print(primos_hasta(100))

#primos shorted
primos_hasta = lambda num: [x for x in range(2, num) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primos_hasta(100))
