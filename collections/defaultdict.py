from collections import defaultdict

# Define a defaultdict with default type int (which defaults to 0)
dd = defaultdict(int)

# Accessing a missing key just creates it with the default value
dd['key'] += 1

print(dd['key'])  # 1
