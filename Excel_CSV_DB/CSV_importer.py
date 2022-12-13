# -*- coding: ansi -*-
# import sqlite3
import pandas as pd

# cbanco de dados.
#con = sqlite3.connect('Lancamentos_Gerais.FULL.db')

# entrada - data Frame
df = pd.read_csv('Lancamentos_Gerais.FULL.csv')
print(df)

# df.to_sql(df ,con, index=False,if_exists="replace")


#con.commit()
#con.close()