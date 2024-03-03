import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame for the student with student_id 101 and select 'name' and 'age' columns
    return students[students['student_id'] == 101][['name', 'age']]

# Example usage:
data = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}
students_df = pd.DataFrame(data)

# Get the name and age of the student with student_id 101
student_101_data = selectData(students_df)

print(student_101_data)