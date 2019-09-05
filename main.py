'''filtrado de ruido'''
import scipy as sp
from scipy import signal
#*****************
'''FFT'''
from scipy.fftpack import fft
''''''

'''TA LIBRARY (VORTEX, ETC)'''
''' https://github.com/bukosabino/ta '''
from ta import *
import ta 
''''''

'''SINGLETON DE RESULTADOS'''
import ResultTabs as rt
from subprocess import Popen

'''ESTRATEGIAS'''
import estrategia1
import os

import subprocess
import threading
import time
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')
import multiprocessing as mp 
from multiprocessing import Process, Queue
import dataHandler
import kivy
#kivy.require('1.11.0')
import finplot as fplt
from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
Config.set('graphics', 'width', '1900')
Config.set('graphics', 'height', '1000')
Config.write()
#from kivy.core.window import Window
#Window.size = (1900, 1000)
import numpy as np
import datetime
from datetime import timedelta
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import matplotlib
import matplotlib.pyplot as plt

#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
#from mpl_finance import candlestick_ohlc
import requests
import pandas as pd
import datetime as datetime
#import matplotlib.dates as mdates
from kivy.uix.treeview import TreeViewLabel, TreeView
from kivy.uix.scrollview import ScrollView  
from kivy.uix.button import Button
  # input system window size
#Window.fullscreen = True
#librerias propias
#import fileManager
import talib
import dataHandler as dt
#matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')

Builder.load_file('SimpleKivy4.kv')
#import matplotlib.pyplot as plt

#labels = ['datetime', 'Open', 'High', 'Low', 'Close']
#ohlc_df=pd.DataFrame.from_records(ohlc, columns=labels)
#ohlc_df = fileManager.get_test()

lol = dt.quotes_general[['time','open','close','high','low','volume']]
lol = lol.astype({'time':'datetime64[ns]'})
lol.time = lol.time + pd.DateOffset(hours=5)
datex = ''

#devuelve 9m de cualquier fecha
#con entrada standart 2019-02-07 08:00:00
def get_9am(fecha):
    res = fecha  + timedelta(hours=1) + timedelta(minutes = 30)
    return res

def get_frac_8to9(df, desde, hasta):
    #df = get_dataframe()
    #df['Date'] = pd.to_datetime(df['Date'])
    fr = df[(df.index > desde) & (df.index <= hasta)]
    return fr
def get_test(df):
    #df = get_dataframe()
    #df['Date'] = pd.to_datetime(df['Date'])
    fr = df[(df.index > '2019-02-07 08:00:00') & (df.index <= '2019-02-07 09:00:00')]
    return fr

def next_8am(df, indice_actual):
    indice_actual = indice_actual+timedelta(hours=24)
    #nonlocal pri 
    pri = indice_actual
    #print ( pri)
    return get_frac_8to9(df, (indice_actual),(indice_actual+timedelta(hours=25)+timedelta(minutes=30)) )


    ''' NUEVAAA'''

def fechas_max_min(df):
    primera , ultima = df['time'].min(), df['time'].max()
    return primera, ultima

def fechas_disponibles(df):
    '''TODO'''
    fechas = pd.date_range(start=df['time'].min(),end=df['time'].max(), freq='D',normalize=True)
    #for e in fechas:   
    return fechas

def plotea_dia(df):
    lol = df
    ax,ax2,ax3 = fplt.create_plot('NASDAQ', rows=3)
    candle_src = fplt.PandasDataSource(lol[['time','open','close','high','low']])
    fplt.candlestick_ochl(candle_src, ax=ax)
    fplt.plot(lol['time'], lol['close'].rolling(25).mean(), ax=ax, color='#0000ff', legend='ma-25')
    df['rnd'] = np.random.normal(size=len(df))
    fplt.plot(df['time'], df['rnd'], ax=ax2, color='#992277', legend='stuff')
    fplt.set_y_range(ax2, -4.4, +4.4) # fix y-axis range

    # finally a volume bar chart in our third plot
    volume_src = fplt.PandasDataSource(lol[['time','open','close','volume']])
    fplt.volume_ocv(volume_src, ax=ax3)

    # we're done
    fplt.show()
    pass

def show_day():
    #lol = df
    temp = lol 
    #temp = self.get_frac_df(temp,)
    ax,ax2,ax3 = fplt.create_plot('NASDAQ', rows=3)
    candle_src = fplt.PandasDataSource(lol[['time','open','close','high','low']])
    fplt.candlestick_ochl(candle_src, ax=ax)
    fplt.plot(lol['time'], lol['close'].rolling(25).mean(), ax=ax, color='#0000ff', legend='ma-25')
    #df['rnd'] = np.random.normal(size=len(df))
    #fplt.plot(df['time'], df['rnd'], ax=ax2, color='#992277', legend='stuff')
    #fplt.set_y_range(ax2, -4.4, +4.4) # fix y-axis range
    # finally a volume bar chart in our third plot
    volume_src = fplt.PandasDataSource(lol[['time','open','close','volume']])
    fplt.volume_ocv(volume_src, ax=ax3)
    # we're done
    fplt.show()
    
def xxx(instance):
    #popen
    pass
    
class MyWidget(BoxLayout):
    def __init__(self):
        super(MyWidget, self).__init__()
        boton1 = Button(text='ANTERIOR 8AM', font_size=16,size_hint_y=0.06)
        #boton1.bind(on_press=self.callback_borra)
        #boton1.bind(on_press=plotea_adelante)
        #self.ids.plot.add_widget(boton1)
        
        boton2 = Button(text='SIGUIENTE 8AM', font_size=16,size_hint_y=0.06)
        #boton2.bind(on_press=self.callback_botton2)
        #boton2.bind(on_press=plotea_adelante)
        #self.ids.plot.add_widget(boton2)
        
        #self.figura = plt.gcf()
        #self.ids.plot.add_widget(FigureCanvasKivyAgg(self.figura))
        
        #self.ids.plot.add_widget(canvas)
        self.fecha = ''
        self.cargaDatos()
        '''IMPORTANTE : DATOS LIGADOS A CLASE: TRABAJAR SOLO ACA'''
        self.marketdata = lol  
        self.play()

    def cargaDatos(self):
        datos =[]# fileManager.get_available_filepaths()
        layout = GridLayout(cols=1, spacing=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for (filename,path) in datos:
            btn = Button(text=str(filename), size_hint_y=None, height=25 )
            btn.bind(on_press=self.callback)
            layout.add_widget(btn)
        self.ids.datos.add_widget(layout)
    #SECCIOND DE CALLBACKS
    def fechas_disponiblesx(self):
        self.ids.his.clear_widgets()
        t = fechas_disponibles(lol)
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        self.fechas = t
        print (t)
        print (t[0])
        i=0
        for e in t:
            y = Button(text=str(i)+'-'+str(e), font_size=13,size_hint_y=None, height = Window.height * .05)
            #y.bind(on_press=self.test)
            y.bind(on_press=self.show_day_plot)
            #y.bind(on_press=show_day)
            #y.bind(on_press=xxx)
            self.ids.his.add_widget(y)
            i = i+1
            #layout.add_widget(y)
        #pass

    '''BOTON: RUN ESTRATEGY'''
    def runEstrategy(self):
        #re = estrategia1.Estrategia()
        #re.init()
        #re.runStrategy()
        '''AGREGA DATOS RESULTANTES A HOJA VACIA'''
        Popen('python estrategia1.py')


        print (rt.Singleton.getInstance().result)
        #print (re.columna)
        #os.system('python ' + str(estrategia1))
    
    def plotResults(self, df):
        #itera cada columna posible dentro del resultado
        for column in df:
            pass


    '''procesamiento de fft'''
    '''implementado en show day plot()'''
    def plot_fft(self, dataframe,column):
        N = len(dataframe[column])
        T = 1.0/800.0
        yf = fft(dataframe[column])
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
        plt.grid()
        plt.show()
        #pass

    '''procesamiento de data'''
    '''implementado en: constructor'''
    def play(self):
        '''************************'''
        '''AGREGA TUS WEADAS ACAAAA'''
        '''************************'''
        self.marketdata['sma200'] = self.marketdata['close'].rolling(200).mean()
        self.marketdata['filtered'] = sp.signal.medfilt(self.marketdata['close'],21) 
        self.marketdata['vortexn'] = ta.vortex_indicator_neg(self.marketdata.high,self.marketdata.low,
                                        self.marketdata.close,fillna=True,n=14)
        self.marketdata['vortexp'] = ta.vortex_indicator_pos(self.marketdata.high,self.marketdata.low,
                                        self.marketdata.close,fillna=True,n=14)
        #self.marketdata['']
        #print (self.marketdata)
        #pass

    '''PLOTEA INFO DE UN DIA - EVENTO BOTON'''
    '''bindeado en botones de dias'''
    def show_day_plot(self, instance):
        aux = int(instance.text.split('-')[0])
        #print ('fechaaa')
        #print (aux)
        
        
        '''TERMINA TUS WEADAS ACA'''
        #print (self.marketdata)
        #temp = pd.date_range(start=temp['time'][self.fechas[0]], end=temp['time'][self.fechas[1]], freq='D')
        #print (self.fechas[0])
        #print (self.fechas[0],self.fechas[1])
        #datex = self.fechas[3]
        desde = self.fechas[aux] + timedelta(hours=5)
        hasta = desde + timedelta(hours=24)
        temp = self.marketdata[(self.marketdata.time > desde) & (self.marketdata.time <= hasta)]
        #print (temp)
        #print (temp['time'][self.fecha])
        #temp = self.get_frac_df(temp,)
        #print ('actualizado')
        
        #print ('SELECCIONADO')
        #print (temp)
        #print (temp.dtypes)

        '''TODO :MEJORA EL FFT que agrege en la ventana izquierda en matplotlib'''
        #self.plot_fft(temp,'filtered')

        ax,ax2,ax3 = fplt.create_plot('NASDAQ', rows=3 )#,maximize=True)
        try:
            '''CANDLESTICK CHARTS'''
            
            candle_src = fplt.PandasDataSource(temp[['time','open','close','high','low']])
            fplt.candlestick_ochl(candle_src, ax=ax,draw_body=True,draw_shadow=True)
            fplt.plot(temp['time'], temp['sma200'], ax=ax, color='#0000ff', legend='ma-200')
            fplt.plot(temp['time'], temp['filtered'], ax=ax, color='#ff00ff', legend='filtrado',width=2)
            
            '''VOLUMEN CHARTS'''
            volume_src = fplt.PandasDataSource(temp[['time','open','close','volume']])
            fplt.volume_ocv(volume_src, ax=ax2)
            
            '''INTERMEDIOS'''
            #te = np.random.normal(size=len(temp))
            #fplt.plot(temp['time'], te, ax=ax2, color='#001177', legend='vortex pos')
            #fplt.plot(temp['time'], temp['vortex_n'], ax=ax2, color='#ff0000', legend='vortex neg')
            #fplt.set_y_range(ax2, -4.4, +4.4) # fix y-axis range
            # draw some random crap on our second plot
            #temp['rnd'] = np.random.normal(size=len(temp))
            #print (temp.vortexn)
            #fplt.plot(temp['time'], temp['vortexn'], ax=ax3, color='#992277', legend='stuff')
            #fplt.set_y_range(ax3, -10.4, +10.7) # fix y-axis range
            # finally a volume bar chart in our third plot
           
            fplt.show()
            #pass
        except Exception as e: 
            print(e)
        pass
        

    def get_frac_df(self, df, desde, hasta):
        #df = get_dataframe()
        #df['Date'] = pd.to_datetime(df['Date'])
        fr = df[(df.index > desde) & (df.index <= hasta)]
        return fr
    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)
        self.ids.seleccionado.text = instance.text
        #fileManager.selected_path = fileManager.path + instance.text
        #fileManager.selected_file = instance.text

    def showquestion(self):
        with open("question.txt","r") as f:
            filetext = f.read()
            self.ids['label1'].text = filetext

    def showanswer(self):
        with open("answer.txt","r") as f:
            filetext = f.read()
            self.ids['label2'].text = filetext

class myApp(App):
    def build(self):
        return MyWidget()
    def on_pause(self): 
        return True
    def on_resume(self): 
        pass


if __name__ in ('__main__', '__android__'): 
    myApp().run()



