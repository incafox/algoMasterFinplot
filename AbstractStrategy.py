from abc import ABC , abstractmethod
import dataHandler as dt
import pandas as pd

class AbstractStrategy(ABC):
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        '''DATA > LOS DATOS , RESULT: DATAFRAME DE RESULTADOS PARA CALCULOS Y MARCADORES'''
        self.data = dt.quotes_general[['time','open','close','high','low','volume']]
        self.data = self.data.astype({'time':'datetime64[ns]'})
        self.data.time = self.data.time + pd.DateOffset(hours=5)
        self.result = self.data[['time']]

    @abstractmethod
    def runStrategy(self):
        '''para que se use por boton'''
        self.init()
        for index, row in self.data.iterrows():
            self.handle(row['open'],row['high'],row['low'],row['close'])
            #print(row['c1'], row['c2'])
        pass

    @abstractmethod
    def init(self):
        print ('abm init')
        pass
    @abstractmethod
    def handleAll(self):
        '''Apply some operation over all the data'''
        
        pass
    @abstractmethod
    def handle(self, open,high,low,close):
        '''Manage the last quotes from the data'''
        print ('abm handle')
        pass

