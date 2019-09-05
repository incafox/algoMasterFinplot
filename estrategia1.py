import AbstractStrategy
import pandas as pd 
import numpy as np
import ResultTabs as rt


class Estrategia(AbstractStrategy.AbstractStrategy):
    

    '''init: setup del inicio'''
    def init(self):
        #print ('init')
        self.columna = []
        self.indice = 0
        rt.Singleton.getInstance().result['tmr'] = np.nan
        #pass#return ''

    '''HANDLE: para cada quote'''
    def handle(self, quote):
        print (self.lastQuote.volume)
        if (self.lastQuote.volume > 200):
            self.columna.append(True)
            #rt.Singleton.getInstance().result['tmr'][self.indice]  = True
            #rt.Singleton.getInstance().result['gaa'] = True
        else :
            self.columna.append(False)
            #rt.Singleton.getInstance().result['tmr'][self.indice]  = False
        
        #print (len(self.columna) , (rt.Singleton.getInstance().result['close']))
        #rt.Singleton.getInstance().result['tmr'][self.indice] = pd.Series(self.columna, index =rt.Singleton.getInstance().result.index ) 
        self.indice += 1
        
        #print (rt.Singleton.getInstance().isWorking)
        #pass

    


#crea la estrategia
temp = Estrategia()

#inicializa la estrategia
temp.init()

#loop de la estrategia
temp.runStrategy()

rt.Singleton.getInstance().result['tmr'] = temp.columna
print (rt.Singleton.getInstance().result)
print('gffdfgsfgs')

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
