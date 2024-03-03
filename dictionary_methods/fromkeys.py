# fromkeys()

people: list[str] = ['Mario', 'Luigi', 'James']

# For default value None
users: dict = dict.fromkeys(people, None)

# For default value as an empty string
users_with_empty_string: dict = dict.fromkeys(people, '')

# For default value as 0
users_with_zero: dict = dict.fromkeys(people, 0)

print(users)  # Output: {'Mario': None, 'Luigi': None, 'James': None}
print(users_with_empty_string)  # Output: {'Mario': '', 'Luigi': '', 'James': ''}
print(users_with_zero)  # Output: {'Mario': 0, 'Luigi': 0, 'James': 0}
