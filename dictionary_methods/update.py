# update()

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'James'}

# old way to do this
# users.update({2: 'Bob', 3: 'James\'s sister'})

# new syntax
# print(users | {10: 'Spam', 11: 'Eggs'})

# hard code
users |= {10: 'Spam', 11: 'Eggs'}
print(users)

