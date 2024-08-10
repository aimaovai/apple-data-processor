def computeStatistics(df, column='Close'):
    max_value = df[column].max()
    min_value = df[column].min()
    avg_value = df[column].mean()
    
    return {
        "max": max_value,
        "min": min_value,
        "average": avg_value
    }
