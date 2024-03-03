import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # Pivot the table so that cities are columns and months are rows
    return weather.pivot(index='month', columns='city', values='temperature')

# Example usage:
weather_data = {
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville',
             'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'May',
              'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
}
weather_df = pd.DataFrame(weather_data)

# Pivot the weather data
pivoted_weather = pivotTable(weather_df)
pivoted_weather

print(pivoted_weather)