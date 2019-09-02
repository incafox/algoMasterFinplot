from abc import ABC , abstractmethod
import dataHandler as dt
import pandas as pd
import abc

class AbstractStrategy(ABC):
    
    def __init__(self):
        super().__init__()
        self.data = dt.quotes_general[['time','open','close','high','low','volume']]
        self.data = self.data.astype({'time':'datetime64[ns]'})
        self.data.time = self.data.time + pd.DateOffset(hours=5)
        self.result = self.data[['time']]
    

    #@abc.abstractmethod
    def runStrategy(self):
        '''para que se use por boton'''
        self.init()
        for index, quote in self.data.iterrows():
            self.lastQuote = quote
            self.handle(self.lastQuote)
            #print(row['c1'], row['c2'])
        pass

    @abstractmethod
    def init(self):
        print ('abm init')
        pass
    
    @abstractmethod
    def handle(self, quote):
        '''Manage the last quotes from the data'''
        print ('abm handle')
        pass

