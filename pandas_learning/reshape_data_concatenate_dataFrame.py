import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # Concatenate df1 and df2 vertically
    return pd.concat([df1, df2], ignore_index=True)

# Example usage:
df1_data = {
    'student_id': [1, 2, 3, 4],
    'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
    'age': [8, 6, 15, 17]
}
df2_data = {
    'student_id': [5, 6],
    'name': ['Leo', 'Alex'],
    'age': [7, 7]
}

df1 = pd.DataFrame(df1_data)
df2 = pd.DataFrame(df2_data)

# Concatenate the tables
combined_df = concatenateTables(df1, df2)
combined_df

print(combined_df)