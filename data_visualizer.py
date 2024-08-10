import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

def plotCandleStick(df, title='Candlestick Chart'):
    df['Datetime'] = pd.to_datetime(df['Week'].astype(str) + "-1")
    df.set_index('Datetime', inplace=True)

    mpf.plot(df, type='candle', volume=True, title=title)
    plt.show()
