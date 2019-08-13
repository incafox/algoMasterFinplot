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
#matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')

Builder.load_file('SimpleKivy4.kv')
#import matplotlib.pyplot as plt

#labels = ['datetime', 'Open', 'High', 'Low', 'Close']
#ohlc_df=pd.DataFrame.from_records(ohlc, columns=labels)
#ohlc_df = fileManager.get_test()


def ocho_am_primera_aparicion(df):
    primera = ''
    ultima = ''
    control = False
    for index, row in df.iterrows():
        #print (index.strftime("%Y-%m-%d %H:%M:%S"))
        #print ('main  ' , index.strftime("%Y-%m-%d %H:%M:%S"))
        if (index.strftime("%H:%M:%S")=='07:50:00'):
            #print ('debug   ' , index.strftime("%Y-%m-%d %H:%M:%S"))
            if (control == False) :primera = index#.strftime("%Y-%m-%d %H:%M:%S")
            control = True
            ultima = index #.strftime("%Y-%m-%d %H:%M:%S")
            
        #print(row['c1'], row['c2'])
    return primera, ultima

def get_next_8am(df, desde):
    primera = ''
    ultima = ''
    control = False
    for index, row in df.iterrows():
        #print (index.strftime("%Y-%m-%d %H%M%S"))
        #print ('main  ' , index.strftime("%Y-%m-%d %H:%M:%S"))
        if (index.strftime("%Y-%m-%d %H:%M:%S").split(' ')[-1]=='07:50:00'):
            #print ('debug   ' , index.strftime("%Y-%m-%d %H:%M:%S"))
            primera = index#.strftime("%Y-%m-%d %H:%M:%S")
            return
            
        #print(row['c1'], row['c2'])
    return primera
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



''' indicadores '''





def plotea_adelante(instance):
    pass
  
class MyWidget(BoxLayout):
    def __init__(self):
        super(MyWidget, self).__init__()
        boton1 = Button(text='ANTERIOR 8AM', font_size=16,size_hint_y=0.06)
        boton1.bind(on_press=self.callback_borra)
        boton1.bind(on_press=plotea_adelante)
        #self.ids.plot.add_widget(boton1)
        
        boton2 = Button(text='SIGUIENTE 8AM', font_size=16,size_hint_y=0.06)
        boton2.bind(on_press=self.callback_botton2)
        boton2.bind(on_press=plotea_adelante)
        #self.ids.plot.add_widget(boton2)
        
        #self.figura = plt.gcf()
        #self.ids.plot.add_widget(FigureCanvasKivyAgg(self.figura))
        
        #self.ids.plot.add_widget(canvas)

        self.cargaDatos()

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
    def callback_borra(self, instance):
        #self.remove_widget(self.canvas)
        #quotes = next_8am(quotes_general,pri)
        #self.figura.clf()
        #pri += (timedelta(hours=24))
        #print (quotes)
        #print (pri)
        pass
    def callback_botton2(self, instance):
        #quotes = next_8am(quotes_general,pri)
        #self.figura.clf()
        #print (quotes)
        #pri += (timedelta(hours=24))
        #print (pri)
        pass

    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)
        self.ids.seleccionado.text = instance.text
        fileManager.selected_path = fileManager.path + instance.text
        fileManager.selected_file = instance.text

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