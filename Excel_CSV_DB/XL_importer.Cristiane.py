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

excel_dataframe = excel_file.parse(sheet_name='matriculas_90')
excel_dataframe.to_sql("matriculas_90", conn, if_exists="replace")

excel_dataframe = excel_file.parse(sheet_name='matriculas_89')
excel_dataframe.to_sql("matriculas_89", conn, if_exists="replace")

excel_dataframe = excel_file.parse(sheet_name='matriculas_88')
excel_dataframe.to_sql("matriculas_88", conn, if_exists="replace")

conn.commit()
conn.close()