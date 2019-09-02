import AbstractStrategy
import pandas as pd 
import numpy as np

class Estrategia(AbstractStrategy.AbstractStrategy):
 
    
    def handle(self, quote):
        print (self.lastQuote.volume)
        #print ('estrategia gaaaa')
        pass

    def init(self):
        print ('init')
        pass#return ''

temp = Estrategia()
temp.init()
#temp.handle(temp.lastQuote)
#print (temp.data)
temp.runStrategy()