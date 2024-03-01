import pandas as pd
import sqlite3
import re
data_base = 'PDW.db'
conn = sqlite3.connect(data_base, check_same_thread=False)
df = pd.read_sql('select * from LANCAMENTOS_GERAIS', conn)
conn.close()
print (len(df))
print(df)
############################################################################
# ok funciona
df['Debito_tmp'] = df["Debito"].map(str)
df5 = df[~df["Debito_tmp"].str.contains('^[0-9]', regex= True, na=True)]
print(df5) 

df['Credito_tmp'] = df["Credito"].map(str)
df6 = df[~df["Credito_tmp"].str.contains('^[0-9]', regex= True, na=True)]
print(df6) 

df['Data_tmp'] = df["Data"].map(str)
df7 = df[~df["Data_tmp"].str.contains('^[0-9]', regex= True, na=True)]

############################################################################
## EXECICIOS experimentais
df2=df[df["Debito"] == 132.58]
print (len(df2))
print(df2)

regex = '[a-z][A-Z]'

df3 = df[~df.Debito.str.contains('[a-z][A-Z]', regex= True, na=True)]
df4 = df[~df["Debito"].str.contains('[a-z][A-Z]', regex= True, na=True)]

var = 'Debito'
df5 = df[~df[f"{var}"].str.contains('[a-z][A-Z]', regex= True, na=True)]


list(df.columns.values)
or
list(df)

print("\nWhether Alphabetic values present in company_code column?")
df['debito_is_alpha'] = list(map(lambda x: x.isalpha(), df['Debito']))
df['credito_is_alpha'] = list(map(lambda x: x.isalpha(), df['Credito']))
df['Tipo_is_alpha'] = list(map(lambda x: x.isalpha(), df['TIPO']))
print(df)