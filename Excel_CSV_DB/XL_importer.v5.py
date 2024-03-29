"""
Dependencies: 
pip install pandas
pip install xlsxwriter
pip install xlrd
pip install openpyxl
pip install sqlalchemy
pip install numpy
pip install pyinstaller
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
# Pput Threads on Loader process
# FIX output messages
# command line parameters ( directories, input file name)
# GUI Interface
# Configuratin file ?
#
#
####################################################################################

"""

import sqlite3
import pandas as pd
import datetime
import numpy as np


def general_entries_CVS_exportator(dataBaseFile, dir_out, file_Out, table_Name):
    connection = sqlite3.connect(dataBaseFile)
    file_full_path = dir_out + file_Out + '.v2'
    print(f"Exporting {file_full_path} to file(s) ")
    sqlStatment = "SELECT substr (LG.DATA, 9,2 ) || '-' || substr (LG.DATA, 6,2 ) || '-' || substr(LG.DATA, 1,4)  AS Quando " \
                  ", LG.Tipo as 'Tipo' " \
                  ", LG.DESCRICAO  as 'Descricao/Lancamento' " \
                  ", replace (LG.Credito, '.', ',') as 'Credito' " \
                  ", replace (LG.DEBITO, '.', ',') as 'Debito' " \
                  ", ''''||cast (mes as text) as 'Mes' " \
                  ", ''''||cast (ano as text) as 'Ano' " \
                  ", ''''||cast (mesAno as text )  as 'Mes/Ano' " \
                  ", LG.ORIGEM  as Origem " \
                  " FROM LANCAMENTOS_GERAIS LG ORDER  BY DATA DESC ; "
    df_out = pd.read_sql(sqlStatment, connection)
    # df_out.to_excel(file_full_path + '.xlsx', sheet_name=table_Name, index=False)
    df_out.to_csv(file_full_path + '.csv', sep=';', index=False, encoding='ansi')

    print(f'Excel export(s) for table "{table_Name}" has been created successfully!')
    connection.close()

def xlsx_report_generator(Sqlite_database, dir_out, file_name, write_multiple_files):
    print('Exporting Summarized data ... .. .  ')
    connection = sqlite3.connect(Sqlite_database)
    file_full_path = dir_out + file_name + '.v2.' + 'xlsx'
    lista_consultas = []
    if write_multiple_files :
        xlsx_writer = pd.ExcelWriter(file_full_path, engine='xlsxwriter', date_format='dd/mm/yyyy')

    lista_consultas.append(["select * from Historicogeral where  date(SUBSTR(Referencia,4,4)||'-'||SUBSTR(Referencia,1,2)||'-'||'01') >= date('now','-13 month');" \
                               ,"HistoricoGeral12Meses"])
    lista_consultas.append(["select * from HistoricoGeral;", "HistoricoGeral"])
    lista_consultas.append(["select * from HistoricoAnual;", "HistoricoAnual"])
    lista_consultas.append(["select tipo as Categoria , sum(debito) as Valor , count(1) as QTD from LANCAMENTOS_GERAIS" \
                            " where Data between date('now','-1 month')  and date('now') and debito > 0 group by tipo "\
                            " order by 2 desc;", "Ultimos30Dias"])
    lista_consultas.append(["SELECT substr (LG.DATA, 9,2 ) || '/' || substr (LG.DATA, 6,2 ) || '/' || substr(LG.DATA, 1,4)  AS Quando " \
                  ", LG.Tipo as 'Tipo' " \
                  ", LG.DESCRICAO  as 'Descricao/Lancamento' " \
                  ", replace (LG.Credito, '.', ',') as 'Credito' " \
                  ", replace (LG.DEBITO, '.', ',') as 'Debito' " \
                  ", ''''||cast (mes as text) as 'Mes' " \
                  ", ''''||cast (ano as text) as 'Ano' " \
                  ", ''''||cast (mesAno as text )  as 'Mes/Ano' " \
                  ", LG.ORIGEM  as Origem " \
                  " FROM LANCAMENTOS_GERAIS LG ORDER  BY DATA DESC ; ", "LANCAMENTOS_GERAIS"])

    for k in range(0, len(lista_consultas)):
        consulta = lista_consultas[k]
        sql_statment = consulta[0]
        excel_sheet = consulta[1]
        df_out = pd.read_sql(sql_statment, connection)
        if write_multiple_files:
            message = f'Exporting Sheet {excel_sheet} to {file_full_path}'
            df_out.to_excel(xlsx_writer, sheet_name=excel_sheet, index=False)

        else:
            file_full_path = dir_out + excel_sheet + '.v2.' + 'xlsx'
            message = f'Exporting {file_full_path} to file(s) '
            df_out.to_excel(file_full_path, sheet_name=excel_sheet, index=False)

        print(message)

    connection.close()
    if write_multiple_files:
        xlsx_writer.save()


def data_correjeitor(conexao):
    print(f'Normalizing data on LANCAMENTOS_GERAIS Table ...  ')
    cursor = conexao
    lista_acoes = []
    lista_acoes.append("Update LANCAMENTOS_GERAIS \
       set Mes = strftime ('%m',data )  \
       , Ano = strftime ('%Y',data )  \
       , mesAno = strftime ('%m',data ) ||'/'||strftime ('%Y',data ); ")

    lista_acoes.append("update LANCAMENTOS_GERAIS set credito = 0 where credito is null; ")
    lista_acoes.append("update LANCAMENTOS_GERAIS set debito = 0 where debito is null ;")
    lista_acoes.append("Delete from TiposLancamentos WHERE ( Código IS NULL or Descrição IS NULL) ;")

    lista_acoes.append("update LANCAMENTOS_GERAIS set descricao = replace (descricao,'∴', '.''.')  ;")
    lista_acoes.append("update LANCAMENTOS_GERAIS set descricao = replace (descricao,'ś', '''s')  ;")
    # listaAcoes.append("update LANCAMENTOS_GERAIS set descricao = replace (descricao,'', '''s')  ;")

    for i in range(0, len(lista_acoes)):
        cursor.execute(lista_acoes[i])


def table_truncator(conexao, table_name):
    cursor = conexao
    # Doping EMPLOYEE table if already exists
    cursor.execute("DROP TABLE " + table_name)
    print(f"Table {table_name} dropped... ")


def data_loader(conn, WorkBooks, General_Entries_table, Guindind_Sheet, excel_File):
    sheets_dataframe = WorkBooks.parse(sheet_name=Guindind_Sheet)
    # print (sheets_dataframe)
    # Creating a cursor object using the cursor() method
    table_truncator(conn.cursor(), General_Entries_table)

    print("Running Loader of the Sheets into database Tables ... .. .  ")
    for i, infos in sheets_dataframe.iterrows():
        table_to_load = infos.TABLE_NAME
        isAccounting = infos.ACCOUNTING
        isCleanable = infos.CLEANABLE
        isLoadeable = infos.LOADABLE

        print(f'Step :->  {i + 1} ; Table (Sheet) :-> {table_to_load} ')

        if 'X' == isLoadeable:
            DataFrame = pd.read_excel(excel_File, sheet_name=table_to_load)
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
                GeneralEntriesDF['Origem'] = table_to_load

                # Ja joga os dados limpos na lançamentos gerais
                GeneralEntriesDF.to_sql(General_Entries_table, conn, index=False, if_exists="append")

            ## grava a tabela (UNITÁRIA) do DataFrame do BD
            DataFrame.to_sql(table_to_load, conn, index=False, if_exists="replace")
            conn.commit()


def create_pivot_history_anual(dataBaseFile, typesTable, EntriesTable):
    print('Creating pivot Table for Anual summarized history ... .. . ')
    connection = sqlite3.connect(dataBaseFile)
    ref_anterior = 'MM/YYYY'
    out_table = 'HistoricoAnual'
    sqlStatmentTypes = 'SELECT Código as COD, Descrição as DESC FROM TiposLancamentos ;'
    sqlStatmentSummary = 'select Ano as Referencia, TIPO, sum(Debito) as DEBITOS FROM LANCAMENTOS_GERAIS GROUP BY Ano, TIPO ' \
                         'order by Ano ;'

    df_types = pd.read_sql(sqlStatmentTypes, connection)
    df_summary = pd.read_sql(sqlStatmentSummary, connection)
    dict_hist_base = {'Referencia': '9999'}
    lista_header = ['Referencia']

    for i, DADOS in df_types.iterrows():
        dict_hist_base.update({DADOS.DESC: 0.00})
        lista_header.append(DADOS.DESC)

    lista_full = []
    current_dict = dict_hist_base.copy()

    for j, Fetcher in df_summary.iterrows():
        # print(f'Ano {Fetcher.Referencia} ; Tipo {Fetcher.TIPO}; Valor {Fetcher.DEBITOS}')
        if ref_anterior == Fetcher.Referencia:
            current_dict[Fetcher.TIPO] += Fetcher.DEBITOS
        else:
            if ref_anterior != 'YYYY':
                lista_full.append(current_dict)
            ref_anterior = Fetcher.Referencia
            current_dict = dict_hist_base.copy()
            current_dict['Referencia'] = Fetcher.Referencia

    lista_full.append(current_dict)

    data_to_write = pd.DataFrame(lista_full)
    data_to_write.to_sql(out_table, connection, index=False, if_exists="replace")
    connection.commit()
    connection.close()


def create_pivot_history_full(dataBaseFile, typesTable, EntriesTable):
    print('Creating pivot Table for summarized history ... .. . ')
    connection = sqlite3.connect(dataBaseFile)
    ref_anterior = 'MM/YYYY'
    out_table = 'HistoricoGeral'
    sql_statment_types = 'SELECT Código as COD, Descrição as DESC FROM TiposLancamentos ;'
    sql_statment_summary = 'select MesAno as Referencia, TIPO, sum(Debito) as DEBITOS FROM LANCAMENTOS_GERAIS GROUP BY MesAno, TIPO ' \
                           'order by Ano , Mes  ;'

    df_types = pd.read_sql(sql_statment_types, connection)
    df_summary = pd.read_sql(sql_statment_summary, connection)
    dict_hist_base = {'Referencia': '99/9999'}
    lista_header = ['Referencia']

    for i, DADOS in df_types.iterrows():
        dict_hist_base.update({DADOS.DESC: 0.00})
        lista_header.append(DADOS.DESC)

    lista_full = []
    current_dict = dict_hist_base.copy()

    for j, Fetcher in df_summary.iterrows():
        if ref_anterior == Fetcher.Referencia:
            current_dict[Fetcher.TIPO] += Fetcher.DEBITOS
        else:
            if ref_anterior != 'MM/YYYY':
                lista_full.append(current_dict)
            ref_anterior = Fetcher.Referencia
            current_dict = dict_hist_base.copy()
            current_dict['Referencia'] = Fetcher.Referencia

    lista_full.append(current_dict)
    data_to_write = pd.DataFrame(lista_full)
    data_to_write.to_sql(out_table, connection, index=False, if_exists="replace")
    connection.commit()
    connection.close()


def main():
    # Environment / Variables
    # current date and time
    current_dt = datetime.datetime.now()
    now = current_dt.strftime("%Y%m%d.%H%M%S")

    work_dir = 'G:/Meu Drive/PDW/'
    input_file = work_dir + 'PDW.xls'
    output_name = 'PDW_REPORTS'
    sqlite_database = work_dir + 'PDW.' + now + '.db'
    sqlite_database = work_dir + 'PDW.db'
    guindind_sheet = 'GUIDING'
    types_of_entries = 'TiposLancamentos'
    general_entries_table = 'LANCAMENTOS_GERAIS'

    # Debugging
    print("===============================================")
    print(f'Excel Sheet  Input file :-> {input_file}' )
    print(f'Output SQLite3 Database :-> {sqlite_database}')
    print(f'Guidind Excel Sheet     :-> {guindind_sheet}')
    print("===============================================")
    print("Personal DataWare House Process Starting")

    data_base = sqlite3.connect(sqlite_database)
    work_books = pd.ExcelFile(input_file)

    data_loader(data_base, work_books, general_entries_table, guindind_sheet, input_file)
    data_correjeitor(data_base.cursor())
    data_base.commit()
    data_base.close()

    create_pivot_history_full(sqlite_database, types_of_entries, general_entries_table)

    create_pivot_history_anual(sqlite_database, types_of_entries, general_entries_table)

    general_entries_CVS_exportator(sqlite_database, work_dir, general_entries_table + '.FULL', general_entries_table)

    xlsx_report_generator(sqlite_database, work_dir, output_name, True)

    print("Personal DataWare House processes ended")
    print("===============================================")


if __name__ == '__main__':
    main()

## EOP
