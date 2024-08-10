# main.py
import pandas as pd
from data_cleaner import cleanData, findDuplicatesOutOfOrder
from data_analyzer import computeStatistics
from data_filter import filterByAverageVolume
from data_aggregator import aggregateWeekly
from data_visualizer import plotCandleStick

def main():
    # Load the data
    df = pd.read_csv('time_series_data.csv', header=0)
    df = df.rename(columns={"Date": "Datetime",
                        "AAPL.Open":"Open",
                        "AAPL.High": "High",
                        "AAPL.Low": "Low",
                        "AAPL.Close": "Close",
                        "AAPL.Volume": "Volume",
                        "AAPL.Adjusted": "Adjusted"})

    # Clean the data
    df_cleaned = cleanData(df)
    duplicates = findDuplicatesOutOfOrder(df_cleaned)
    print(f"Out of order or duplicate records:\n{duplicates}")

    # Compute statistics
    statistics = computeStatistics(df_cleaned)
    print(f"Data statistics:\nMax: {statistics['max']}\nMin: {statistics['min']}\nAverage: {statistics['average']}")

    # Filter the data by average volume and save it
    df_filtered = filterByAverageVolume(df_cleaned)

    # Aggregate the data weekly and save it
    weekly_data = aggregateWeekly(df_filtered)

    # Plot the data as candlestick chart
    plotCandleStick(weekly_data)

if __name__ == "__main__":
    main()

# %%
