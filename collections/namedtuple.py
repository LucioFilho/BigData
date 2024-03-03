# namedtuple

from collections import namedtuple

# Define a namedtuple type
Person = namedtuple('Person', 'name age country')

# Create a namedtuple instance
person = Person(name = "John", age = 30, country = 'USA')

print(person.name)  # John
print(person.age)  # 30
print(person.country)  # USA