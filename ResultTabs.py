'''SINGLETON: grabara todos los resultados de la estrategia'''


import pandas as pd 
import dataHandler as dt
class Singleton:
    __instance = None
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        self.result = dt.quotes_general[['time','open','close','high','low','volume']]
        self.result = self.result.astype({'time':'datetime64[ns]'})
        self.result.time = self.result.time + pd.DateOffset(hours=5)
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
    
    def addColumn(self,df,name):
        self.result[name] = df
        pass

s = Singleton()
print (s)

s = Singleton.getInstance()
print (s)

s = Singleton.getInstance()
print (s)