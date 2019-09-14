'''CLASE ABSTRACTA PARA UNA ORDEN EN GENERAL'''

import numpy as np
import pandas as pd 

class Order():

    def __init__(self, index,timeTab, time , inicio, stopLimit, takeProfit, type, maxDuration):
        self.type = type
        self.stopLimit = stopLimit
        self.takeProfit = takeProfit
        self.inicio = inicio
        '''
        timeTab: tabla de incide para cuadrar datos
        time  : tiepo donde se inicio la operacion
        inicio : precion donde se inicio la operacion
        type : buy / sell
        '''
        #super().__init__(*args, **kwargs)
        #crea tabla de registro
        self.result = timeTab
        #agrega tabla de ploteo
        self.result[time] = np.nan
        self.result[time][index] = inicio
        pass

    '''graba operacion en una tabla de pandas'''
    def saveAndEnd(self):
        pass

    def update(self, time, price):
        if (self.type=='buy'):
            if (price>=self.takeProfit):
                self.total = price - self.inicio 
                self.saveAndEnd()
            else:
                pass
            pass
        elif (type=='sell'):
            pass
        pass
    ''''''
    
    