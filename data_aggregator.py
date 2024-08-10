import pandas as pd

def aggregateWeekly(df):
    df['Week'] = pd.to_datetime(df['Datetime']).dt.to_period('W')
    weekly_data = df.groupby('Week').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum'
    }).reset_index()

    weekly_data.to_csv('weekly_data.csv', index=False)
    
    return weekly_data