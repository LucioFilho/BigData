import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicate rows based on the 'email' column, keeping the first occurrence
    return customers.drop_duplicates(subset='email', keep='first')

# Example usage:
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
}
customers_df = pd.DataFrame(data)

# Drop duplicate emails
unique_customers = dropDuplicateEmails(customers_df)
unique_customers

print(unique_customers)