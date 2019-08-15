import pandas as pd
import dataHandler as dt  
import talib as ta 
#import ulib 
#accede a datos
df = dt.quotes_general[['time','open','close','high','low','volume']]
#format time
df = df.astype({'time':'datetime64[ns]'})
#pasa a hora local
df.time = df.time + pd.DateOffset(hours=5)

print (df)

'''ENTRADA: arreglo [true,true,false,true,true,true ...]'''
'''SALIDA:arreglo [true,false,false,true,false,false ...] '''
'''hace valida la primera incidencia'''
'''esto sirve para hacer una sola compra/venta'''
'''true es compra o venta'''
def one_oportunity_filter(df,column):
    step=True
    temporal = False
    for index, row in df.iterrows():
        if (temporal==True and row[column]==True):
            
            
        #if (row[column]==True and step==True ):
            #step=False
        temporal=row[column]
        # print(row[column])


#procesa todos los indicadores necesarios

class indicatorManager():

    def __init__(self, df):
        self.dataframe = df
    
    def add_indicator(self,indicator_name):

        if (indicator_name=='rsi'):
            pass
        elif (indicator_name=='macd'):
            pass 
        elif (indicator_name == 'vortex'):
            pass
        else :
            pass
        #self.dataframe.





#