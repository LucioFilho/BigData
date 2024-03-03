# namedtuple for Data Parsing
'''namedtuple makes your code more readable and self-documenting 
when dealing with complex data structures. 
Imagine parsing a CSV file where each row represents a student's information.'''

from collections import namedtuple
import csv

# Define a namedtuple type for students
Student = namedtuple('Student', 'name age grade')

students = []

# Update this path to the exact location where you saved 'students.csv'
file_path = 'F:\CURSOS\PYTHON\python-learning\collections\students.csv'

with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        students.append(Student(*row))

# Accessing students' information
    for student in students:
        print(f'{student.name}, {student.age} years old, actual grade: {student.grade}')
