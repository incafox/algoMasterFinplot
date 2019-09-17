'''CLASE ABSTRACTA PARA UNA ORDEN EN GENERAL'''

import numpy as np
import pandas as pd 

class Order():

    #el nombre de la columna sera la fecha como identificador unico
    def __init__(self, index,timeTab, time , inicio, stopLimit, takeProfit, type, maxDuration):
        self.type = type
        self.stopLimit = stopLimit
        self.takeProfit = takeProfit
        self.inicio = inicio
        self.time = time
        self.operationFInished = False
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
        self.result[self.time] = np.nan
        #self.result[self.time][index] = inicio
        pass

    '''graba final de contrato en una tabla de pandas'''
    def saveAndEnd(self, lastQuote, book_buy, book_sell):
        if (self.type == 'buy'):
            #graba la salida
            self.result[self.time][lastQuote.time] = self.inicio + self.takeProfit
            #graba en archivo el resultado
            book_buy[str(self.time)] = self.result
        elif (self.type == 'sell'):
            pass
        pass

    def update(self, lastQuote, book_buy, book_sell):
        print ("updating orders ... :v")
        if (self.type=='buy' and self.operationFInished==False):
            if (lastQuote.close>=self.takeProfit):
                self.total = lastQuote.close - self.inicio 
                self.saveAndEnd(lastQuote,book_buy, book_sell)
                self.operationFInished = True
                return
            else:
                return
            pass
        elif (type=='sell' and self.operationFInished == False):
            pass
        pass
    ''''''
    
    