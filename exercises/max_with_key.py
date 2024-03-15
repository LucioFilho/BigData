# show the max ocurrence of a value
x = [1, 2, 1, 3, 4, 1, 2, 4, 1]

most = max(set(x), key=x.count)
print(most)
