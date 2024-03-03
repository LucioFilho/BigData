# Combining Data Structures
''' You can combine these data structures for more complex data management tasks, 
such as using defaultdict to create a nested data structure that counts occurrences 
of items within categories.'''

from collections import defaultdict, Counter

# Categorizing and counting fruits by color
fruits = [('red', 'apple'), ('yellow', 'banana'), ('red', 'cherry'), ('green', 'apple')]
fruit_colors = defaultdict(Counter)

for color, fruit in fruits:
    fruit_colors[color][fruit] += 1

for color, fruits in fruit_colors.items():
    print(f"{color}: {dict(fruits)}")
