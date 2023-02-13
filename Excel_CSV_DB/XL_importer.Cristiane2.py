"""
pip install pandas
pip install xlrd
pip install openpyxl
pip install sqlalchemy

"""


import sqlite3
import pandas as pd

conn=sqlite3.connect('C:/TEMP/Cristiane/Matriculas.db')
excel_file = pd.ExcelFile('C:/TEMP/Cristiane/Pasta1.xlsx')

excel_dataframe = excel_file.parse(sheet_name='resultado_66')
excel_dataframe.to_sql("resultado_66", conn, if_exists="replace")

excel_dataframe = excel_file.parse(sheet_name='resultado_65')
excel_dataframe.to_sql("resultado_65", conn, if_exists="replace")

excel_dataframe = excel_file.parse(sheet_name='resultado_64')
excel_dataframe.to_sql("resultado_64", conn, if_exists="replace")

conn.commit()
conn.close()