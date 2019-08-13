import dataHandler as dt

import finplot as fplt
import numpy as np
import pandas as pd
import requests

# pull some data
symbol = 'USDT-BTC'
url = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=%s&tickInterval=fiveMin' % symbol
data = requests.get(url).json()

# format it in pandas
df = pd.DataFrame(data['result'])
df = df.rename(columns={'T':'time', 'O':'open', 'C':'close', 'H':'high', 'L':'low', 'V':'volume'})
df = df.astype({'time':'datetime64[ns]'})

# create three plots
ax,ax2,ax3 = fplt.create_plot(symbol, rows=3)
lol = dt.quotes_general[['time','open','close','high','low','volume']]
lol = lol.astype({'time':'datetime64[ns]'})

# plot candle sticks
candle_src = fplt.PandasDataSource(lol[['time','open','close','high','low']])
#candle_src = fplt.PandasDataSource(lol)

fplt.candlestick_ochl(candle_src, ax=ax)

print (df.info(verbose=True))
print (lol.info(verbose=True))
#print (df[['time','open','close','high','low']])
#print (dt.quotes_general[['Date','open','close','high','low']])
# put an MA in there
fplt.plot(lol['time'], lol['close'].rolling(25).mean(), ax=ax, color='#0000ff', legend='ma-25')

# place some dumb markers
#hi_wicks = df['high'] - df[['open','close']].T.max().T
#df.loc[(hi_wicks>hi_wicks.quantile(0.99)), 'marker'] = df['close']
#fplt.plot(df['time'], df['marker'], ax=ax, color='#000000', style='^', legend='dumb mark')

# draw some random crap on our second plot
df['rnd'] = np.random.normal(size=len(df))
fplt.plot(df['time'], df['rnd'], ax=ax2, color='#992277', legend='stuff')
fplt.set_y_range(ax2, -1.4, +1.7) # fix y-axis range

# finally a volume bar chart in our third plot
volume_src = fplt.PandasDataSource(lol[['time','open','close','volume']])
fplt.volume_ocv(volume_src, ax=ax3)

# we're done
fplt.show()
