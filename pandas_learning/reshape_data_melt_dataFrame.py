import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    # Melt the DataFrame from wide to long format
    melted_report = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    return melted_report

# Example usage:
report_data = {
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
}
report_df = pd.DataFrame(report_data)

# Reshape the report data
reshaped_report = meltTable(report_df)
reshaped_report

print(reshaped_report)