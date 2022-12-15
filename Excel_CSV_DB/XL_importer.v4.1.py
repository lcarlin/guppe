# -*-encoding:ansi-*-
"""
Dependencies: 
pip install pandas
pip install xlrd
pip install openpyxl
pip install sqlalchemy
pip install numpy
####################################################################################
# Author  : Carlin, Luiz A. .'. 
# e-mail  : luiz.carlin@gmail.com
# Date    : 13-DEC-2022 
# purpose :  Import Sheets from Excel Workbook into SQlite3 Tables
#
####################################################################################
# Version control
# Date    #    What     #   Who
#
####################################################################################
# Todo List
# Separar o Loader em uma função especifica
# criar tabelas Pivots Historicos
# Gerar Export de tabelas Pivots Históricos
# Gerar exports deiversos 
####################################################################################

"""

import sqlite3
import pandas as pd
import datetime
import numpy as np


def data_xPortator1(dataBaseFile, dir_out, file_Out, table_Name):
    connection = sqlite3.connect(dataBaseFile)
    fileFullPath = dir_out + file_Out + 'v2.xlsx'
    print(f"Exporting {fileFullPath} to file ")
    sqlStatment = "SELECT substr (LG.DATA, 9,2 ) || '-' || substr (LG.DATA, 6,2 ) || '-' || substr(LG.DATA, 1,4)  AS Quando " \
                  ", LG.Tipo as 'Tipo' " \
                  ", LG.DESCRICAO  as 'Descricao/Lancamento' " \
                  ", replace (LG.Credito, '.', ',') as 'Credito' "\
                  ", replace (LG.DEBITO, '.', ',') as 'Debito' "\
                  ", ''''||cast (mes as text) as 'Mes' "\
                  ", ''''||cast (ano as text) as 'Ano' "\
                  ", ''''||cast (mesAno as text )  as 'Mes/Ano' " \
                  ", LG.ORIGEM  as Origem "\
            " FROM LANCAMENTOS_GERAIS LG ORDER  BY DATA DESC ; "
    df_out = pd.read_sql(sqlStatment, connection)
    df_out.to_excel(fileFullPath,  sheet_name=table_Name, index=False )
    df_out.to_csv(dir_out + file_Out + 'v2.csv', sep=';', encoding='ansi')

    print(f'Excel Sheet {table_Name} has been created successfully!')
    connection.close()


def data_correjeitor(conexao):
    print(f'Normalizing data on LANCAMENTOS_GERAIS Table ...  ')
    cursor = conexao
    listaAcoes = []
    listaAcoes.append("Update LANCAMENTOS_GERAIS \
       set Mes = strftime ('%m',data )  \
       , Ano = strftime ('%Y',data )  \
       , mesAno = strftime ('%m',data ) ||'/'||strftime ('%Y',data ); ")

    listaAcoes.append("update LANCAMENTOS_GERAIS set credito = 0 where credito is null; ")
    listaAcoes.append("update LANCAMENTOS_GERAIS set debito = 0 where debito is null ;")
    listaAcoes.append("Delete from TiposLancamentos WHERE ( Código IS NULL or Descrição IS NULL) ;")
    for i in len(listaAcoes):
        cursor.execute(listaAcoes[i])


def table_truncator(conexao, table_name):
    cursor = conexao
    # Doping EMPLOYEE table if already exists
    cursor.execute("DROP TABLE " + table_name)
    print(f"Table {table_name} dropped... ")

def main():
    # Environment / Variables
    # current date and time
    currentDT = datetime.datetime.now()
    now = currentDT.strftime("%Y%m%d.%H%M%S")

    Work_dir = 'G:/Meu Drive/PDW/'
    excel_File = Work_dir + 'PDW.xls'
    Sqlite_database = Work_dir + 'PDW.' + now + '.db'
    Sqlite_database = Work_dir + 'PDW.db'
    Guindind_Sheet = 'GUIDING'

    # Debugging
    print("===============================================")
    print(excel_File)
    print(Sqlite_database)
    print(Guindind_Sheet)
    print("===============================================")

    conn = sqlite3.connect(Sqlite_database)
    WorkBooks = pd.ExcelFile(excel_File)
    sheets_dataframe = WorkBooks.parse(sheet_name=Guindind_Sheet)
    # print (sheets_dataframe)
    General_Entries_table = 'LANCAMENTOS_GERAIS'

    # Creating a cursor object using the cursor() method
    # table_truncator(conn.cursor(), General_Entries_table)

    print("Running Loader of the Sheets into database Tables ... .. .  ")
    for i, infos in sheets_dataframe.iterrows():
        table_To_Load = infos.TABLE_NAME
        isAccounting = infos.ACCOUNTING
        isCleanable = infos.CLEANABLE
        isLoadeable = infos.LOADABLE

        print(f'Step :->  {i + 1} ; Table (Sheet) :-> {table_To_Load} ')

        if 'X' == isLoadeable:
            DataFrame = pd.read_excel(excel_File, sheet_name=table_To_Load)
            if 'X' == isAccounting and 'X' == isCleanable:
                ## limpa registros com os Tipos Nulos
                DataFrame['TIPO'].replace('', np.nan, inplace=True)
                DataFrame.dropna(subset=['TIPO'], inplace=True)

                ## limpa registros com as Datas Nulas
                DataFrame['Data'].replace('', np.nan, inplace=True)
                DataFrame.dropna(subset=['Data'], inplace=True)

                # Faz Drop da ulimta coluna (Marcação, subtotal essas coisas
                # DataFrame.drop(DataFrame.columns[5],  inplace=True, axis=1)

                GeneralEntriesDF = DataFrame[["Data", "TIPO", "DESCRICAO", "Credito", "Debito"]].copy()
                GeneralEntriesDF['Mes'] = 'MM'
                GeneralEntriesDF['Ano'] = 'YYYY'
                GeneralEntriesDF['MesAno'] = 'MM/YYYY'
                GeneralEntriesDF['Origem'] = table_To_Load

                # Ja joga os dados limpos na lançamentos gerais
                GeneralEntriesDF.to_sql(General_Entries_table, conn, index=False, if_exists="append")

            ## grava a tabela (UNITÁRIA) do DataFrame do BD
            DataFrame.to_sql(table_To_Load, conn, index=False, if_exists="replace")
            conn.commit()

    #    if 'X' == isAccounting:
    data_correjeitor(conn.cursor())
    conn.commit()
    conn.close()

    data_xPortator1(Sqlite_database, Work_dir, General_Entries_table + '.FULL', General_Entries_table)


if __name__ == '__main__':
    main()

## EOP
