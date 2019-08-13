import pandas as pd 


global quotes_general
dateparse = lambda x: pd/datetime.strptime(x, '%d/%m/%Y %H%M%S')
#quotes_general = pd.read_csv('C:\\Users\\REAL_\\Desktop\\micro-nasdaq\\MNQU19Minute.csv',
quotes_general = pd.read_csv('MNQU19Minute.csv',
                        skiprows=1,
#                     index_col=0,
                     #date_parser=dateparse,
                     parse_dates={'Date': [0,1]},
                     infer_datetime_format=True,header=None,dayfirst=True#,nrows=250
         )#lol = pd.to_datetime(quotes_general.index.astype(str), format='%Y-%m-%d %H:%M:%S')
#lol = pd.to_datetime(quotes_general.index.dt.strftime('%Y-%m'))
quotes_general = quotes_general.rename(columns={'Date':'time',2:'open',3:'high',4:'low',5:'close',6:'volume'})
#print (lol)
#tmr = pd.to_datetime(quotes_general.index).dt.strftime('%Y-%d-%m %H:%M:%S')
#print(tmr)


quotes_general.time = pd.to_datetime(quotes_general.time)

#quotes_general.index = pd.to_datetime(quotes_general.index)

print (quotes_general.dtypes)
global pri 
global ult
#pri,ult = ocho_am_primera_aparicion(quotes_general)
#print ("fechitas")
#print (pri,ult)
#lol = pd.to_datetime(quotes_general.index.astype(str), format='%Y-%m-%d %H:%M:%S')
#lol = pd.to_datetime(quotes_general.index.dt.strftime('%Y-%m'))
#print (lol)
#tmr = pd.to_datetime(quotes_general.index).dt.strftime('%Y-%d-%m %H:%M:%S')
#print(tmr)
#print (quotes_general[[index,2,3,4,5]])
