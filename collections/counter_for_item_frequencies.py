# Counter for Item Frequencies
'''Counter is particularly useful for counting occurrences of elements in a collection, 
such as finding the most common words in a document.'''

from collections import Counter

# Counting word occurrences in a sentence
sentence = "this is a common sentence and it is a simple sentence"
words = sentence.split()

word_counts = Counter(words)
most_common_three = word_counts.most_common(3)

print(most_common_three)  # [('sentence', 2), ('is', 2), ('a', 2)]
