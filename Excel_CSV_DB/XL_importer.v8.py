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
# Date       #    What                      #   Who
# 2022-12-26 # Merge With Version 6.1 and 7 # Carlin, Luiz A. .'.
####################################################################################
# Todo List
# GUI Interface
#
#
#
####################################################################################
"""

import sqlite3
import pandas as pd
import datetime
import numpy as np
import configparser
import os
import threading


def parallel_df(db_file, xls_file, config_dict, general_out_table, index):
    db_connection = sqlite3.connect(db_file)
    tmp_table_name = config_dict['table_to_load']
    print(f'   . .. ... .... Begin of Thread Number :-> {index}  ; Table/Sheet Name :-> {tmp_table_name} ')
    data_frame = pd.read_excel(xls_file, sheet_name=config_dict['table_to_load'])
    if 'X' == config_dict['isAccounting'] and 'X' == config_dict['isCleanable']:
        # limpa registros com os Tipos Nulos
        data_frame['TIPO'].replace('', np.nan, inplace=True)
        data_frame.dropna(subset=['TIPO'], inplace=True)
        # limpa registros com as Datas Nulas
        data_frame['Data'].replace('', np.nan, inplace=True)
        data_frame.dropna(subset=['Data'], inplace=True)
        general_entries_df = data_frame[["Data", "TIPO", "DESCRICAO", "Credito", "Debito"]].copy()
        general_entries_df.insert(1, 'DIA_SEMANA', np.nan)
        general_entries_df['Mes'] = 'MM'
        general_entries_df['Ano'] = 'YYYY'
        general_entries_df['MesAno'] = 'MM/YYYY'
        general_entries_df['Origem'] = config_dict['table_to_load']
        # Ja joga os dados limpos na lançamentos gerais
        general_entries_df.to_sql(general_out_table, db_connection, index=False, if_exists="append")

    # grava a tabela (UNITÁRIA) do data_frame do BD
    data_frame.to_sql(config_dict['table_to_load'], db_connection, index=False, if_exists="replace")
    db_connection.commit()
    db_connection.close()
    print(f'   . .. ... .... End of Thread Number :-> {index}  ; Table/Sheet Name :-> {tmp_table_name} ')


def data_loader_parallel(data_base, general_entries_table, guindind_sheet, excel_file):
    conn = sqlite3.connect(data_base, check_same_thread=False)
    work_books = pd.ExcelFile(excel_file)
    sheets_dataframe = work_books.parse(sheet_name=guindind_sheet)
    table_droppator(conn.cursor(), general_entries_table)
    conn.commit()
    jobs = list()
    print("Running Loader of the Sheets into database Tables ... .. .  ")
    for i, infos in sheets_dataframe.iterrows():
        dict_config = {'table_to_load': infos.TABLE_NAME,
                       'isAccounting': infos.ACCOUNTING,
                       'isCleanable': infos.CLEANABLE,
                       'isLoadeable': infos.LOADABLE}

        tmp_table_name = dict_config['table_to_load']
        print(f'   . .. ... Step:->  {i + 1:04} ; Table (Sheet) :-> {tmp_table_name} ')
        if 'X' == dict_config['isLoadeable']:
            # thread = threading.Thread(target=parallel_df(conn, excel_File, dict_config, General_Entries_table, i + 1))
            thread = threading.Thread(target=parallel_df,
                                      args=(data_base, excel_file, dict_config, general_entries_table, i + 1))
            jobs.append(thread)

    print(f'   . .. ... Starting Multi-Threaging processing')
    for m in jobs:
        m.start()

    print(f'   . .. ... Waiting for Threads to End ')
    # Ensure all of the threads have finished
    for index, tread in enumerate(jobs):
        print(f'   ... .. . Index Of :-> {index}')
        thread.join()

    print(f'   . .. ... All threads has ended ')
    data_correjeitor(conn.cursor())
    print(f'   . .. ... Data-Loader Done !!! !! ! ')
    conn.commit()
    conn.close()


def general_entries_cvs_exportator(data_base_file, dir_out, file_out, table_name):
    connection = sqlite3.connect(data_base_file)
    file_full_path = dir_out + file_out + '.v2'
    print(f"Exporting {file_full_path} to file(s) ")
    sqlStatment = "SELECT substr (LG.DATA, 9,2 )||'-'||substr(LG.DATA,6,2 )||'-' || substr(LG.DATA, 1,4) AS Quando " \
                  ", LG.DIA_SEMANA as 'Dia da Semana' " \
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
    df_out.to_csv(file_full_path + '.csv', sep=';', index=False, encoding='ansi')
    print(f'Excel export(s) for table "{table_name}" has been created successfully!')
    connection.close()


def xlsx_report_generator(sqlite_database, dir_out, file_name, write_multiple_files, out_extension):
    print('Exporting Summarized data ... .. .  ')
    connection = sqlite3.connect(sqlite_database)
    file_full_path = dir_out + file_name + '.' + out_extension
    lista_consultas = []
    if write_multiple_files:
        xlsx_writer = pd.ExcelWriter(file_full_path, engine='xlsxwriter', date_format='yyyy-mm-dd')

    lista_consultas.append([
        "select * from Historicogeral where  date(SUBSTR(Referencia,4,4)||'-'||SUBSTR(Referencia,1,2)||'-'||'01') >= date('now','-13 month');" \
        , "HistoricoGeral12Meses"])
    lista_consultas.append(["select * from HistoricoGeral;", "HistoricoGeral"])
    lista_consultas.append(["select * from HistoricoAnual;", "HistoricoAnual"])
    lista_consultas.append(["select tipo as Categoria, sum(debito) as Valor , count(1) as QTD from LANCAMENTOS_GERAIS" \
                            " where Data >= date('now','-1 month')  and Data <= date('now', '+1 day') and debito > 0 " \
                            " group by tipo order by 2 desc;", "Ultimos30Dias"])
    lista_consultas.append(
        ["SELECT substr (LG.DATA, 1,4 ) || '-' || substr (LG.DATA, 6,2 ) || '-' || substr(LG.DATA, 9,2) AS Quando " \
         ", LG.DIA_SEMANA as 'Dia da Semana' " \
         ", LG.Tipo as 'Tipo' " \
         ", LG.DESCRICAO  as 'Descricao/Lancamento' " \
         ", replace (LG.Credito, '.', ',') as 'Credito' " \
         ", replace (LG.DEBITO, '.', ',') as 'Debito' " \
         ", ''''||cast (mes as text) as 'Mes' " \
         ", ''''||cast (ano as text) as 'Ano' " \
         ", ''''||cast (mesAno as text )  as 'Mes/Ano' " \
         ", LG.ORIGEM  as Origem " \
         " FROM LANCAMENTOS_GERAIS LG ORDER  BY DATA DESC ; ", "LANCAMENTOS_GERAIS"])
    lista_consultas.append(["select Ano || ' - ' || Mes as 'Referência', count(1) as 'Total' " \
                            ", round( cast (count(1) as float)  / ( case Mes when '01' then 31" \
                            " when '02' then 28 when '03' then 31 when '04' then 30 when '05' then 31" \
                            " when '06' then 30 when '07' then 31 when '08' then 31 when '09' then 30" \
                            " when '10' then 31 when '11' then 30 when '12' then 31 end ),2) as 'Por Dia'" \
                            " from LANCAMENTOS_GERAIS group by  Ano || ' - ' || Mes " \
                            " order by  Ano || ' - ' || Mes desc ;", "Iterações_Mensais"])

    for k in range(0, len(lista_consultas)):
        consulta = lista_consultas[k]
        sql_statment = consulta[0]
        excel_sheet = consulta[1]
        df_out = pd.read_sql(sql_statment, connection)
        if write_multiple_files:
            message = f'   . .. ... Step: {k + 1:04} :-> Exporting Sheet {excel_sheet} to {file_full_path}'
            df_out.to_excel(xlsx_writer, sheet_name=excel_sheet, index=False)

        else:
            file_full_path = dir_out + excel_sheet + '.v2.' + out_extension
            message = f'   . .. ... Step: {k + 1:04} :-> Exporting {file_full_path} to file(s) '
            df_out.to_excel(file_full_path, sheet_name=excel_sheet, index=False)

        print(message)

    connection.close()
    if write_multiple_files:
        # xlsx_writer.save()
        xlsx_writer.close()


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
    lista_acoes.append("update LANCAMENTOS_GERAIS set descricao = replace (descricao,'', '''s')  ;")
    lista_acoes.append("UPDATE LANCAMENTOS_GERAIS " \
                       "  SET DIA_SEMANA =   case cast (strftime('%w', Data ) as integer) " \
                       "  when 0 then 'Domingo' " \
                       "  when 1 then 'Segunda-Feira' " \
                       "  when 2 then 'Terça-Feira' " \
                       "  when 3 then 'Quarta-Feira' " \
                       "  when 4 then 'Quinta-Feira' " \
                       "  when 5 then 'Sexta-Feira' " \
                        " when 6 then 'Sábado' " \
                       "  else 'INVALIDO' end " \
                       "    where DIA_SEMANA IS NULL ; ")

    for i in range(0, len(lista_acoes)):
        print(f'   . .. ... Step: {i + 1:04}')
        cursor.execute(lista_acoes[i])


def table_droppator(conexao, table_name):
    cursor = conexao
    cursor.execute("DROP TABLE IF EXISTS " + table_name)
    print(f"Table {table_name} dropped... ")


def data_loader(data_base, general_entries_table, guindind_sheet, excel_file):
    conn = sqlite3.connect(data_base)
    work_books = pd.ExcelFile(excel_file)
    sheets_dataframe = work_books.parse(sheet_name=guindind_sheet)
    table_droppator(conn.cursor(), general_entries_table)
    print("Running Loader of the Sheets into database Tables ... .. .  ")
    for i, infos in sheets_dataframe.iterrows():
        table_to_load = infos.TABLE_NAME
        is_accounting = infos.ACCOUNTING
        is_cleanable = infos.CLEANABLE
        is_loadeable = infos.LOADABLE
        print(f'   . .. ... Step: {i + 1:04} ; Table (Sheet) :-> {table_to_load} ')
        if 'X' == is_loadeable:
            data_frame = pd.read_excel(excel_file, sheet_name=table_to_load)
            if 'X' == is_accounting:
                data_frame['TIPO'].replace('', np.nan, inplace=True)
                data_frame['Data'].replace('', np.nan, inplace=True)
                if  'X' == is_cleanable:  ## ATENÇÃO A ISSO AQUI 
                    # limpa registros com os Tipos Nulos
                    data_frame.dropna(subset=['TIPO'], inplace=True)
                    # limpa registros com as Datas Nulas
                    data_frame.dropna(subset=['Data'], inplace=True)
                    
                general_entries_df = data_frame[["Data", "TIPO", "DESCRICAO", "Credito", "Debito"]].copy()
                general_entries_df.insert(1, 'DIA_SEMANA', np.nan)
                general_entries_df['Mes'] = 'MM'
                general_entries_df['Ano'] = 'YYYY'
                general_entries_df['MesAno'] = 'MM/YYYY'
                general_entries_df['Origem'] = table_to_load
                # Ja joga os dados limpos na lançamentos gerais
                general_entries_df.to_sql(general_entries_table, conn, index=False, if_exists="append")

            # grava a tabela (UNITÁRIA) do DataFrame do BD
            data_frame.to_sql(table_to_load, conn, index=False, if_exists="replace")
            conn.commit()

    data_correjeitor(conn.cursor())
    conn.commit()
    conn.close()


def create_pivot_history_anual(data_base_file, types_table, entries_table):
    print('Creating pivot Table for Anual summarized history ... .. . ')
    connection = sqlite3.connect(data_base_file)
    ref_anterior = 'MM/YYYY'
    out_table = 'HistoricoAnual'
    sql_statment_types = 'SELECT Código as COD, Descrição as DESC FROM TiposLancamentos ;'
    sql_statment_summary = 'select Ano as Referencia, TIPO, sum(Debito) as DEBITOS FROM LANCAMENTOS_GERAIS ' \
                           ' GROUP BY Ano, TIPO order by Ano ;'
    df_types = pd.read_sql(sql_statment_types, connection)
    df_summary = pd.read_sql(sql_statment_summary, connection)
    dict_hist_base = {'Referencia': '9999'}
    lista_header = ['Referencia']
    for i, DADOS in df_types.iterrows():
        dict_hist_base.update({DADOS.DESC: 0.00})
        lista_header.append(DADOS.DESC)

    lista_full = []
    current_dict = dict_hist_base.copy()
    for j, Fetcher in df_summary.iterrows():
        if ref_anterior != Fetcher.Referencia:
            lista_full.append(current_dict)
            ref_anterior = Fetcher.Referencia
            current_dict = dict_hist_base.copy()
            current_dict['Referencia'] = Fetcher.Referencia

        current_dict[Fetcher.TIPO] += Fetcher.DEBITOS

    lista_full.append(current_dict)  # writes the last line into the list
    dev_null = lista_full.pop(0)  # remove the 1st reference
    data_to_write = pd.DataFrame(lista_full)
    data_to_write.to_sql(out_table, connection, index=False, if_exists="replace")
    connection.commit()
    connection.close()


def create_pivot_history_full(data_base_file, types_table, entries_table):
    print('Creating pivot Table for summarized history ... .. . ')
    connection = sqlite3.connect(data_base_file)
    ref_anterior = 'MM/YYYY'
    out_table = 'HistoricoGeral'
    sql_statment_types = 'SELECT Código as COD, Descrição as DESC FROM TiposLancamentos ;'
    sql_statment_summary = 'select MesAno as Referencia, TIPO, sum(Debito) as DEBITOS FROM LANCAMENTOS_GERAIS ' \
                           ' GROUP BY MesAno, TIPO order by Ano, Mes, TIPO desc ;'
    df_types = pd.read_sql(sql_statment_types, connection)
    df_summary = pd.read_sql(sql_statment_summary, connection)
    dict_hist_base = {'Referencia': '99/9999'}
    lista_header = ['Referencia']
    for i, DADOS in df_types.iterrows():
        dict_hist_base.update({DADOS.DESC: 0})
        lista_header.append(DADOS.DESC)

    lista_full = []
    current_dict = dict_hist_base.copy()
    for j, Fetcher in df_summary.iterrows():
        if ref_anterior != Fetcher.Referencia:
            lista_full.append(current_dict)
            ref_anterior = Fetcher.Referencia
            current_dict = dict_hist_base.copy()
            current_dict['Referencia'] = Fetcher.Referencia

        current_dict[Fetcher.TIPO] += Fetcher.DEBITOS

    lista_full.append(current_dict)
    dev_null = lista_full.pop(0)  # remove the 1st reference
    data_to_write = pd.DataFrame(lista_full)
    data_to_write.to_sql(out_table, connection, index=False, if_exists="replace")
    connection.commit()
    connection.close()


def main():
    # Environment / Variables
    # current date and time
    config = configparser.ConfigParser()
    try:
        print('Reading configuration file ... .. .')
        with open('config.ini') as cfg:
            config.read_file(cfg)

        dir_file_in = config['DIRECTORIES']['DIR_IN']
        dir_file_out = config['DIRECTORIES']['DIR_OUT']

        in_file = config['FILE_TYPES']['INPUT_FILE']
        in_type = config['FILE_TYPES']['TYPE_IN']
        out_type = config['FILE_TYPES']['TYPE_OUT']
        out_db = config['FILE_TYPES']['OUT_DB_FILE']
        output_name = config['FILE_TYPES']['OUT_RPT_FILE']
        db_file_type = config['FILE_TYPES']['DB_FILE_TYPE']
        log_file_cfg = dir_file_out + config['FILE_TYPES']['LOG_FILE']
        
        splitter = config.getint('SETTINGS', 'PARALLELS')
        multithread = config.getboolean('SETTINGS', 'MULTITHREADING')
        overwrite_db = config.getboolean('SETTINGS', 'OVERWRITE_DB')
        run_loader = config.getboolean('SETTINGS', 'RUN_DATA_LOADER')
        run_reports = config.getboolean('SETTINGS', 'RUN_REPORTS')
        multi_rept_file = config.getboolean('SETTINGS', 'RPT_SINGLE_FILE')
        guiding_table = config['SETTINGS']['GUIDING_TABLE']
        types_of_entries = config['SETTINGS']['TYPES_OF_ENTRIES']
        general_entries_table = config['SETTINGS']['GENERAL_ENTRIES_TABLE']
        create_pivot = config['SETTINGS']['CREATE_PIVOT']
        save_discarted_data = config['SETTINGS']['SAVE_DISCARTED_DATA']
        discarted_data_table = config['SETTINGS']['DISCARTED_DATA_TABLE']

        # NOVO02 = config.getboolean('settings', 'SelfDestruction')
    except FileNotFoundError:
        print("Arquivo de configuracao nao encontrado!")
        exit(1)
    except configparser.Error as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)

    started = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    input_file = dir_file_in + in_file + '.' + in_type
    if overwrite_db:
        sqlite_database = dir_file_out + out_db + '.' + db_file_type
    else:
        sqlite_database = dir_file_out + out_db + '.' + datetime.datetime.now().strftime("%Y%m%d.%H%M%S") + '.' + db_file_type

    if not os.path.exists(dir_file_in):
        print(f'The Input Directory {dir_file_in} does not exists  !!! !! !')
        exit(1)

    if not os.path.exists(dir_file_out):
        print(f'The Output Directory {dir_file_out} does not exists ... .. .')
        exit(1)

    if not os.path.isfile(input_file):
        print(f'The Input Load File {input_file} does not exists in the Input Directory {dir_file_in} ... .. .')
        exit(1)

    # begin of log block
    last_run_date = 'none'
    log_file_exists = os.path.isfile(log_file_cfg)
    is_log_empty = False
    if log_file_exists:
        is_log_empty = os.stat(log_file_cfg).st_size == 0
        if is_log_empty:
            print(f'Log File {log_file_cfg} is Empty ')
    else:
        print(f'Log File {log_file_cfg} does Not Exists yet ')
        new_log_file = open(log_file_cfg,'w')
        new_log_file.write('New LOG created at :-> '+ datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") +'\n')
        new_log_file.close()

    log_file = open(log_file_cfg,'r+')
    if not is_log_empty and log_file_exists:
       last_line = log_file.readlines()[-1]
       last_record = last_line.split('|')
       last_run_date = last_record[0]
    # end of LOG block

    print("===============================================")
    print(f'Last RUN Date           :-> {last_run_date}')
    print(f'LOG File                :-> {log_file_cfg} ')
    print(f'Excel Sheet  Input file :-> {input_file}')
    print(f'Output SQLite3 Database :-> {sqlite_database}')
    print(f'Guidind Excel Sheet     :-> {guiding_table}')
    print("===============================================")
    print("Personal DataWare House Process Starting")

    if run_loader:
        if not multithread:
            data_loader(sqlite_database, general_entries_table, guiding_table, input_file)
        else:
            data_loader_parallel(sqlite_database, general_entries_table, guiding_table, input_file)

    if create_pivot:
        create_pivot_history_full(sqlite_database, types_of_entries, general_entries_table)
        create_pivot_history_anual(sqlite_database, types_of_entries, general_entries_table)
    
    if run_reports:
        general_entries_cvs_exportator(sqlite_database, dir_file_out, general_entries_table + '.FULL',
                                       general_entries_table)
        xlsx_report_generator(sqlite_database, dir_file_out, output_name, multi_rept_file, out_type)

    log_line = started + '| Started|' + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")+'| Ended'
    log_file.write(log_line)
    log_file.write('\n')

    print("Personal DataWare House processes ended")
    print("===============================================")


if __name__ == '__main__':
    main()

# EOP
