from collections import Counter

# Create a Counter from a list
cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(cnt)  # Counter({'blue': 3, 'red': 2, 'green': 1})

# Counters support various operations
print(cnt.most_common(2))  # [('blue', 3), ('red', 2)]
