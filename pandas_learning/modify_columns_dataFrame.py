import pandas as pd

def modifySalaries(employees: pd.DataFrame) -> pd.DataFrame:
    # Multiply each salary by 2
    employees['salary'] = employees['salary'] * 2
    return employees

# Example usage:
data = {
    'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
    'salary': [19666, 74754, 62509, 54866]
}
employees_df = pd.DataFrame(data)

# Modify the salaries
updated_employees = modifySalaries(employees_df)
updated_employees

print(updated_employees)