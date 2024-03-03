import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a new column 'bonus' by doubling the values in the 'salary' column
    employees['bonus'] = employees['salary'] * 2
    return employees

# Example usage:
data = {
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
}
employees_df = pd.DataFrame(data)

# Create the bonus column
employees_with_bonus = createBonusColumn(employees_df)
employees_with_bonus

print(employees_with_bonus)