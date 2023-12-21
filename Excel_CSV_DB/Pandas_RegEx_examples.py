import pandas as pd
import sqlite3
import re
data_base = 'PDW.db'
conn = sqlite3.connect(data_base, check_same_thread=False)
df = pd.read_sql('select * from LANCAMENTOS_GERAIS', conn)
print (len(df))

df2=df[df["Debito"] == 132.58]
print (len(df2))
print(df2)

regex = '[a-z][A-Z]'

df3 = df[~df.Debito.str.contains('[a-z][A-Z]', regex= True, na=True)]
df4 = df[~df["Debito"].str.contains('[a-z][A-Z]', regex= True, na=True)]

var = 'Debito'
df5 = df[~df[f"{var}"].str.contains('[a-z][A-Z]', regex= True, na=True)]