import pandas as pd

def cleanData(df):
    # Sort data by date
    df = df.sort_values('Datetime')

    # Drop the duplicates
    df = df.drop_duplicates()

    return df

def findDuplicatesOutOfOrder(df):
    duplicates = df[df.duplicated()]
    return duplicates
