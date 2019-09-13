from abc import ABC , abstractmethod
import glob
#from main import lol#dataHandler as dt
import pandas as pd
import abc
#import ResultTabs as rt
import numpy as np

class AbstractStrategy(ABC):
    
    def __init__(self):
        super().__init__()
        self.data = pd.read_pickle("MNQU19Minute.pkl")#dt.quotes_general[['time','open','close','high','low','volume']]
        #self.data = self.data.astype({'time':'datetime64[ns]'})
        #self.data.time = self.data.time + pd.DateOffset(hours=5)
        self.result = self.data[['time']]
        #self.single = rt.Singleton.getInstance()
        #tabla de resultados
        #rt.Singleton.getInstance().result['t1'] = np.nan
        self.resultados_columnas = []  #almacena columnas de resultados
    #@abc.abstractmethod
    def runStrategy(self):
        #self.single.initWorking()
        '''para que se use por boton'''
        self.init()
        for index, quote in self.data.iterrows():
            self.lastQuote = quote
            self.handle(self.lastQuote)
            #print(row['c1'], row['c2'])
        self.post()
        i = 0
        for e in self.resultados_columnas:
            pass
            #i += 1
            #rt.Singleton.getInstance().result['t'+str(i)] = e
        #self.single.endedWorking()
        pass

    @abstractmethod
    def init(self):
        #print ('abm init')
        pass
    
    @abstractmethod
    def handle(self, quote):
        '''Manage the last quotes from the data'''
        #print ('abm handle')
        pass

    @abstractmethod
    def post(self):
        '''Manage the last quotes from the data'''
        #print ('abm handle')
        pass

     
