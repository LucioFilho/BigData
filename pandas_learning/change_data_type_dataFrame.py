import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # Convert the 'grade' column to integers
    students['grade'] = students['grade'].astype(int)
    return students

# Example usage:
data = {
    'student_id': [1, 2],
    'name': ['Ava', 'Kate'],
    'age': [6, 15],
    'grade': [73.0, 87.0]
}
students_df = pd.DataFrame(data)

# Change the data type of the grade column
updated_students = changeDatatype(students_df)
updated_students


print(updated_students)