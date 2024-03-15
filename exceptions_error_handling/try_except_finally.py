try:
    print('try')
    # print(a)
    print(1/0)
except ZeroDivisionError:
    print('You cannot divide by 0')
except NameError:
    print('Variable does not exist')
else:
    print('the else statment')
finally:
    print('finally...')

# assert
a = 1
assert a == 1