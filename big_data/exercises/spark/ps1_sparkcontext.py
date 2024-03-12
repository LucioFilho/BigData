print('v_10____________________________')

from pyspark import SparkContext

sc = SparkContext()

textFile = sc.textFile('./big_data/exercises/spark/example.txt')

textFile


# ACTIONS

print(f'Collect: {textFile.collect()}')

# print(f'Count: {textFile.count()}')

# print(f'First: {textFile.first()}')

#TRANSFORMATION

#instructions
second = textFile.filter(lambda line: 'second' in line)
second
print(f'Second: {second}')

#applying the instructions
# second.collect()

# print(f'Filter: {second.collect()}')