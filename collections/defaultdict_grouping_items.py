# defaultdict for Grouping Items
'''defaultdict is ideal for grouping items, for instance, 
categorizing words by their first letter or grouping students by their grades.'''

from collections import defaultdict

words = ["apple", "bat", "bar", "atom", "book"]
word_categories = defaultdict(list)

for word in words:
    first_letter = word[0]
    word_categories[first_letter].append(word)

for letter, words in word_categories.items():
    print(f"{letter}: {words}")
