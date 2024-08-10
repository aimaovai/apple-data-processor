# Time Series Processor

This package processes time series data by cleaning, analyzing, filtering, aggregating, and visualizing it. 

## How to Use

1. Place your time series CSV file in the root directory.
2. Run `main.py` to process the data.
3. The filtered data will be saved as `filtered_data.csv`.
4. The aggregated weekly data will be saved as `weekly_data.csv`.
5. A candlestick chart will be generated from the weekly data.

## Modules

- `data_cleaner.py`: Cleans and validates the time series data.
- `data_analyzer.py`: Computes statistical information.
- `data_filter.py`: Filters data based on average volume and adds the day of the week.
- `data_aggregator.py`: Aggregates data on a weekly level.
- `visualizer.py`: Generates candlestick charts.
