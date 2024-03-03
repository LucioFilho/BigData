import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # Rename the columns as specified
    new_columns = {
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }
    return students.rename(columns=new_columns)

# Example usage:
data = {
    'id': [1, 2, 3, 4, 5],
    'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age': [6, 7, 16, 18, 10]
}
students_df = pd.DataFrame(data)

# Rename the columns
updated_students = renameColumns(students_df)
updated_students

print(updated_students)