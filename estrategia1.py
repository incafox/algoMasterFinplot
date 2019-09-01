import AbstractStrategy
import pandas as pd 
import numpy as np

class Estrategia(AbstractStrategy):

    def __init__(self, *args, **kwargs):
        #super().__init__(self, *args, **kwargs)
        pass
    
    def handle(self):
        print ('estrategia')
        pass

    def init(self):
        print ('init')
        pass

temp = Estrategia()
temp.init()
