"""
pip install pandas
pip install xlrd
pip install openpyxl
pip install sqlalchemy

"""


import sqlite3
import pandas as pd

conn=sqlite3.connect('G:/Meu Drive/PDW/PDW.db')
excel_file = pd.ExcelFile('G:/Meu Drive/PDW/PDW.xls')

excel_dataframe = excel_file.parse(sheet_name='ItaU')
excel_dataframe.to_sql("ItaU", conn, if_exists="replace")

excel_dataframe1 = excel_file.parse(sheet_name='TiposLancamentos')
excel_dataframe1.to_sql("TiposLancamentos", conn, if_exists="TiposLancamentos")
"""
excel_dataframe = excel_file.parse(sheet_name='Despesas')
excel_dataframe.to_sql("Despesas", conn, if_exists="Despesas")


excel_dataframe = excel_file.parse(sheet_name='NUBank_Master')
excel_dataframe.to_sql("NUBank_Master", conn, if_exists="NUBank_Master")
"""
conn.commit()
conn.close()