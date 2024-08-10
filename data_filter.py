import pandas as pd
def filterByAverageVolume(df):
    avg_volume = df['Volume'].mean()
    df_filtered = df[df['Volume'] >= avg_volume]
    
    # Add column for actual day of the week
    df_filtered['Day'] = pd.to_datetime(df_filtered['Datetime']).dt.day_name()
    df_filtered.to_csv('filtered_data.csv', index=False)
    return df_filtered
