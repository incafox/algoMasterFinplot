import AbstractStrategy
import pandas as pd 
import numpy as np
import ResultTabs as rt


class Estrategia(AbstractStrategy.AbstractStrategy):
    

    '''init: setup del inicio'''
    def init(self):
        print ('init')
        #pass#return ''

    '''HANDLE: para cada quote'''
    def handle(self, quote):
        print (self.lastQuote.volume)
        print (rt.Singleton.getInstance().isWorking)
        #pass


#crea la estrategia
#temp = Estrategia()

#inicializa la estrategia
#temp.init()

#loop de la estrategia
#temp.runStrategy()

#print (rt.Singleton.getInstance().isWorking)
#print (rt.Singleton.getInstance().isWorking)
#print (rt.Singleton.getInstance().isWorking)
               
#temp.handle(temp.lastQuote)
#print (temp.data)
#temp.runStrategy()

#s = rt.Singleton.getInstance()
#print (s.result)
#s.addColumn(s.result['close'],'holi')
#print (s.result)
