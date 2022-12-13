"""
pip install pandas
pip install xlrd
pip install openpyxl
pip install sqlalchemy

"""


import sqlite3
import pandas as pd

Work_dir = 'G:/Meu Drive/PDW/'
excel_File = Work_dir + 'PDW.xls'
Sqlite_database = Work_dir + 'PDW.FULL.db'
print ("===============================================")
print (excel_File)
print(Sqlite_database)
print ("===============================================")
conn = sqlite3.connect(Sqlite_database)
WorkBooks = pd.ExcelFile(excel_File)

for sheet in WorkBooks.sheet_names:
        print(sheet)
        DataFrame=pd.read_excel('G:/Meu Drive/PDW/PDW.xls',sheet_name=sheet)
        DataFrame.to_sql(sheet,conn, index=False,if_exists="replace")

conn.commit()
conn.close()

## EOP