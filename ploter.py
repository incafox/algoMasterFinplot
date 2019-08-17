import dataHandler as dt
import finplot as fplt
from datetime import timedelta
import pandas as pd

lol = dt.quotes_general[['time','open','close','high','low','volume']]
lol = lol.astype({'time':'datetime64[ns]'})
lol.time = lol.time + pd.DateOffset(hours=5)
#datex = ''
fechas = pd.date_range(start=lol['time'].min(),end=lol['time'].max(), freq='D',normalize=True)
    
def show_day_plot():
    #self.fecha = instance.text
    #print (self.fecha)
    temp = lol 
    #temp = pd.date_range(start=temp['time'][self.fechas[0]], end=temp['time'][self.fechas[1]], freq='D')
    #print (type(self.fechas[0]))
    #print (self.fechas[0],self.fechas[1])
    datex = fechas[3]
    desde = fechas[1] + timedelta(hours=5)
    hasta = desde + timedelta(hours=24)
    temp = lol[(lol.time > desde) & (lol.time <= hasta)]
    print (temp)
    print ('mierdaaa')
    #print (emp['time'][self.fecha])
    #temp = self.get_frac_df(temp,)
    ax,ax2,ax3 = fplt.create_plot('NASDAQ', rows=3)
    candle_src = fplt.PandasDataSource(temp[['time','open','close','high','low']])
    fplt.candlestick_ochl(candle_src, ax=ax)
    fplt.plot(lol['time'], lol['close'].rolling(25).mean(), ax=ax, color='#0000ff', legend='ma-25')
    #subprocess.Popen(['python','ploter.py'])
    #df['rnd'] = np.random.normal(size=len(df))
    #fplt.plot(df['time'], df['rnd'], ax=ax2, color='#992277', legend='stuff')
    #fplt.set_y_range(ax2, -4.4, +4.4) # fix y-axis range

    # finally a volume bar chart in our third plot
    volume_src = fplt.PandasDataSource(temp[['time','open','close','volume']])
    fplt.volume_ocv(volume_src, ax=ax3)
    fplt.show()


show_day_plot()
