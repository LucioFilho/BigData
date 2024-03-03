# Sort complex iterables with sorted()
data = (3, 5, 1, 10, 9)
sorted_data = sorted(data, reverse=True)

print(sorted_data)

# do it instead
data = [{"name": "Max", "age": 6},
        {"name": "Lisa", "age": 20},
        {"name": "Ben", "age": 9}]

sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)

# Sorting a list of integers in ascending order
integers = [5, 3, 1, 8, 7]
sorted_integers = sorted(integers)
print("Sorted Integers:", sorted_integers)

# Sorting a list of strings in alphabetical order
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words)
print("Sorted Words:", sorted_words)

# Sorting a tuple in descending order
tup_data = (3, 5, 1, 10, 9)
sorted_tup_data = sorted(tup_data, reverse=True)
print("Sorted Tuple:", sorted_tup_data)

# Sorting a list of dictionaries by a specific key
people = [
    {"name": "Max", "age": 6},
    {"name": "Lisa", "age": 20},
    {"name": "Ben", "age": 9}
]
# Sort by age in ascending order
sorted_people_by_age = sorted(people, key=lambda x: x["age"])
print("Sorted by age:", sorted_people_by_age)

# Sort by name in alphabetical order
sorted_people_by_name = sorted(people, key=lambda x: x["name"])
print("Sorted by name:", sorted_people_by_name)

# Sorting in descending order usin the 'reverse' parameter
descending_people_by_age = sorted(eople, key=lambda x: x["age"], reverse=True)
print("Descending by age:", descending_people_by_age)

# Always using comprehensions. Not every loop should be a comprehension.
def always_using_comprehensions(a, b, n):
    # matrix product of a, b of length n * n
    return [
        sum(a[n *i + k] * b[n * k + j] for k in range(n))
        for i in range(n)        for j in range(n)
    ]
