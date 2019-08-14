import pandas as pd
import dataHandler as dt  

#accede a datos
df = dt.quotes_general[['time','open','close','high','low','volume']]
#format time
df = df.astype({'time':'datetime64[ns]'})
#pasa a hora local
df.time = df.time + pd.DateOffset(hours=5)

print (df)

#