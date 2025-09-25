"""
####################################################################################
# Author  : Carlin, Luiz A. .'.
# e-mail  : luiz.carlin@gmail.com
# Date    : 13-DEC-2022
# purpose : Import Sheets from Excel Workbook into SQLite3 Tables
#           ET&L -> Extract, Transform & Loader
####################################################################################
# Version control
# Date       # Version #    What                            #   Who
# 2022-12-26 # 8       # Merge With Version 6.1 and 7       # Carlin, Luiz A. .'.
# 2023-04-12 # 9.0.4   # Export date in several formats in  #
#                      # LANCAMENTOS_GERAIS                 # Carlin, Luiz A. .'.
# 2023-04-20 # 9.1.0   # Run dinamic reports based on anual #
#                      # info                               # Carlin, Luiz A. .'.
# 2023-08-23 # 9.1.5   # create Index Main table            # Carlin, Luiz A. .'.
#                      # Do not create intermediate tables  #
#                      #  Anymore for Accounting Sheets     #
#                      # Now the export function            #
#                      #   Just Export data                 #
#                      # New Columns on the main Table      #
# 2023-10-05 # 9.2.0   # Export Transient data from API Tab.# Carlin, Luiz A. .'.
# 2023-12-20 # 9.3.0   # Data Validator: verify if tehe is  # Carlin, Luiz A. .'.
#                      #  Any invalid data on main fields   #
# 2024-04-03 # 9.3.2   # remove INPLACE NPN MAN             # Carlin, Luiz A. .'.
#                      # CHANGES Encoding from ansi CP1252  #
# 2024-04-04 # 9.3.2   # files "MesAno" changed to AnoMEs   # Carlin, Luiz A. .'.
# 2024-05-28 # 9.4.0   # Pivot Table Improvment             # Carlin, Luiz A. .'.
# 2024-08-08 # 9.4.4   # TimeStamp and Separator on LOG     # Carlin, Luiz A. .'.
# 2024-09-02 # 9.5.0   # totaling daily amount of data In   # Carlin, Luiz A. .'.
#                      # General Reports                    #
# 2024-10-03 # 9.6.0   # payment in installments summary    # Carlin, Luiz A. .'.
# 2024-10-22 # 9.6.1   # New Pivot Tables with COUNT of     # Carlin, Luiz A. .'.
#                      # totals                             # Carlin, Luiz A. .'.
# 2024-11-06 # 9.7.0   # Generating summaries of all        # Carlin, Luiz A. .'.
#                      #   accounting tables                #
# 2024-12-09 # 9.7.0   # Genenal Entries Resumes (Y/M)      # Carlin, Luiz A. .'.
# 2025-01-20 # 9.8.0   # Optimizing Data Loader funciont    # Carlin, Luiz A. .'.
# 2025-09-25 # 9.8.1   # put Round at data loader           # Carlin, Luiz A. .'.
####################################################################################
# Current Version : 9.8.1
####################################################################################
# TODO: GUI Interface
# TODO: Use config file as parameters? (done)
# TODO: read encrypted excel file ?
# TODO: Write encrypted Excel file ?
# TODO: Remove parallel items ?
# TODO: be able to use another databases ?
# TODO: Refactor code to be able to use another types od database
# TODO: Version Number in main module (done)
# TODO: Hostname + version in log (done)
# TODO: Put HistoricoGeral table name in Parameter file (done)
# TODO: Put HistoricoAnual table name in Parameter file (done)
# TODO: Create saparated output directories (log, report and database) (done)
# TODO: Transiet data writer/export (done)
# TODO:
# TODO:
# TODO:
####################################################################################
Dependencies:
pip install pandas
pip install xlsxwriter
pip install xlrd
pip install openpyxl
pip install sqlalchemy
pip install numpy
pip install pyinstaller

pip install lxml
pip install tabulate
pip install tables0
pyinstaller -F -i "G:\\Meu Drive\\PDW\\DataWareHouse02.ico" .\\XL_importer.v9.py

"""

import sqlite3
import pandas as pd
import datetime
import numpy as np
import configparser
import os, platform, sys
import threading
import time
import xml.etree.ElementTree as ET
import gzip
import shutil

def split_paymnt_resume(db_file, split_paymnt_table, out_table):
    print('Creating payment in installments Summaries ... .. .  ')
    db_conn = sqlite3.connect(db_file)

    df_parcelamentos = pd.read_sql(f"SELECT * FROM {split_paymnt_table}", db_conn)
    df_parcelamentos['Ano_Mes'] = pd.to_datetime(df_parcelamentos['Data']).dt.to_period('M')
    df_agrupado = df_parcelamentos.groupby('Ano_Mes').agg(Quantidade=('Data', 'size'),
                                                          Valor=('Debito', 'sum')).reset_index()
    df_agrupado['Diff_QTD'] = df_agrupado['Quantidade'].diff().fillna(0)
    df_agrupado['Diff_Vlr'] = df_agrupado['Valor'].diff().fillna(0)
    df_agrupado['Ano_Mes'] = df_agrupado['Ano_Mes'].astype(str)
    df_agrupado['Valor'] = df_agrupado['Valor'].round(2)
    df_agrupado['Diff_Vlr'] = df_agrupado['Diff_Vlr'].round(2)
    df_agrupado.to_sql(out_table, db_conn, index=False, if_exists="replace")


def main(param_file):
    # Environment / Variables
    # current date and time
    start = time.time()
    started = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    current_version = "9.9.0"
    os_pataform = platform.system()

    # if the system is windows then use the below
    # command to check for the hostname
    if os_pataform == "Windows":
        hostname = platform.uname().node
    else:
        # otherwise use the below command
        hostname = os.uname()[1]

    config = configparser.ConfigParser()
    config_file = 'PersonalDataWareHouse.cfg'

    if len(param_file) > 0:
        config_file = param_file

    try:
        print('Reading configuration file ... .. .')
        with open(config_file) as cfg:
            config.read_file(cfg)

        parameters_version = config['SETTINGS']['CURRENT_VERSION']
        if parameters_version != current_version:
            print(f'The version in parameter file {config_file} does not Match')
            print(f'Informed :-> {parameters_version}')
            print(f'Expected :-> {current_version}')
            exit(1)

        dir_file_in = config['DIRECTORIES']['DIR_IN']
        dir_file_out = config['DIRECTORIES']['DIR_OUT']
        dir_log = config['DIRECTORIES']['LOG_DIR']
        dir_db = config['DIRECTORIES']['DATABASE_DIR']

        in_file = config['FILE_TYPES']['INPUT_FILE']
        in_type = config['FILE_TYPES']['TYPE_IN']
        out_type = config['FILE_TYPES']['TYPE_OUT']
        out_db = config['FILE_TYPES']['OUT_DB_FILE']
        output_name = config['FILE_TYPES']['OUT_RPT_FILE']
        db_file_type = config['FILE_TYPES']['DB_FILE_TYPE']
        log_file_cfg = dir_log + config['FILE_TYPES']['LOG_FILE']

        splitter = config.getint('SETTINGS', 'PARALLELS')
        multithread = config.getboolean('SETTINGS', 'MULTITHREADING')
        overwrite_db = config.getboolean('SETTINGS', 'OVERWRITE_DB')
        run_loader = config.getboolean('SETTINGS', 'RUN_DATA_LOADER')
        run_reports = config.getboolean('SETTINGS', 'RUN_REPORTS')
        multi_rept_file = config.getboolean('SETTINGS', 'RPT_SINGLE_FILE')
        guiding_table = config['SETTINGS']['GUIDING_TABLE']
        types_of_entries = config['SETTINGS']['TYPES_OF_ENTRIES']
        general_entries_table = config['SETTINGS']['GENERAL_ENTRIES_TABLE']
        create_pivot = config.getboolean('SETTINGS', 'CREATE_PIVOT')
        save_discarted_data = config.getboolean('SETTINGS', 'SAVE_DISCARTED_DATA')
        discarted_data_table = config['SETTINGS']['DISCARTED_DATA_TABLE']
        full_hist_table = config['SETTINGS']['FULL_PIVOT_TABLE']
        anual_hist_table = config['SETTINGS']['ANUAL_PIVOT_TABLE']
        export_transeient_data = config.getboolean('SETTINGS','EXPORT_TRANSIENT_DATA')
        transient_data_table = config['SETTINGS']['TRANSIENT_DATA_TABLE']
        transient_data_file = config['FILE_TYPES']['TRANSIENT_DATA_FILE']
        origem_dados = config['SETTINGS']['TRANSIENT_DATA_COLUMN']
        other_file_types = config.getboolean('SETTINGS', 'EXPORT_OTHER_TYPES')

        dinamic_reports = config.getboolean('SETTINGS', 'RUN_DINAMIC_REPORT')
        din_report_guinding = config['SETTINGS']['DIN_REPORT_GUIDING']
        dayly_progress = config['SETTINGS']['DAYLY_PROGRESS']

        split_paymnt_table = config['SETTINGS']['SPLT_PAYMNT_TAB']
        out_table = config['SETTINGS']['OUT_RES_PMNT_TAB']
        monthly_summarie = config['SETTINGS']['MONTHLY_SUMMATIES']

        # NOVO02 = config.getboolean('settings', 'SelfDestruction')
    except FileNotFoundError:
        print(f"Configuration file {config_file} not found !")
        exit(1)
    except configparser.Error as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)

    input_file = dir_file_in + in_file + '.' + in_type
    if overwrite_db:
        sqlite_database = dir_db + out_db + '.' + db_file_type
    else:
        sqlite_database = dir_db + out_db + '.' + datetime.datetime.now().strftime(
            "%Y%m%d.%H%M%S") + '.' + db_file_type

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
        new_log_file = open(log_file_cfg, 'w')
        new_log_file.write('New LOG created at :-> ' + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')
        new_log_file.close()

    log_file = open(log_file_cfg, 'r+')
    if not is_log_empty and log_file_exists:
        last_run_date = log_file.readlines()[-1].split('|')[0]
    # end of LOG block
    out_line = ">" + ("=" * 120) + "<"
    print(out_line)
    print(f'Current Version         :-> {current_version}')
    print(f'Last RUN Date           :-> {last_run_date}')
    print(f'Config/INI File         :-> {config_file}')
    print(f'LOG File                :-> {log_file_cfg} ')
    print(f'Excel Sheet  Input file :-> {input_file}')
    print(f'Output SQLite3 Database :-> {sqlite_database}')
    print(f'Guiding Excel Sheet     :-> {guiding_table}')
    print(out_line)
    print("Personal Data Warehouse Processes are Starting | ET&L -> Extract, Transform & Loader !")

    if run_loader:
        print(out_line)
        if not multithread:
            data_loader(sqlite_database, types_of_entries, general_entries_table, origem_dados, guiding_table,
                        input_file,
                        save_discarted_data, discarted_data_table)
        else:
            print(f'Bad, Bad Server. Not donuts for you')
            print(f'Threads are evil. Avoid them.')
            print('')
            print('https://www2.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-1.pdf')
            print('')
            print(
                '    SQLite is threadsafe. We make this concession since many users choose to ignore the advice given in the previous paragraph. ')
            print(
                'But in order to be thread-safe, SQLite must be compiled with the SQLITE_THREADSAFE preprocessor macro set to 1.  ')
            print('Both the Windows and Linux precompiled binaries in the distribution are compiled this way.  ')
            print(
                'If you are unsure if the SQLite library you are linking against is compiled to be threadsafe you can call the sqlite3_threadsafe() interface to find out. ')
            print(' ')
            print('    SQLite is threadsafe because it uses mutexes to serialize access to common data structures.  ')
            print('However, the work of acquiring and releasing these mutexes will slow SQLite down slightly.  ')
            print(
                'Hence, if you do not need SQLite to be threadsafe, you should disable the mutexes for maximum performance.  ')
            print(
                'Under Unix, you should not carry an open SQLite database across a fork() system call into the child process. ')
            print('See the threading mode documentation for additional information. ')
            print(' ')
            exit(1)
            # data_loader_parallel(sqlite_database, types_of_entries, general_entries_table, guiding_table, input_file,
            #                         save_discarted_data, discarted_data_table)

    if create_pivot:
        print(out_line)
        create_pivot_history(sqlite_database, types_of_entries, general_entries_table, full_hist_table,
                             anual_hist_table)
        if dinamic_reports:
            print(out_line)
            create_dinamic_reports(sqlite_database, input_file, din_report_guinding, full_hist_table)

    if run_reports:
        print(out_line)
        monthly_summaries(sqlite_database, general_entries_table, monthly_summarie)

        print(out_line)
        general_entries_file_exportator(sqlite_database, dir_file_out, general_entries_table + '.FULL',
                                        general_entries_table, other_file_types)
        print(out_line)
        split_paymnt_resume(sqlite_database, split_paymnt_table, out_table)
        print(out_line)
        xlsx_report_generator(sqlite_database, dir_file_out, output_name, multi_rept_file, out_type,
                              general_entries_table, dinamic_reports, din_report_guinding, create_pivot,
                              anual_hist_table, full_hist_table, dayly_progress, out_table, monthly_summarie)

    if export_transeient_data:
        print(out_line)
        transient_data_exportator(sqlite_database, dir_file_out, out_type, transient_data_file, transient_data_table,
                                  origem_dados)

    end = time.time()
    total_running_time: str = f"{end - start:7.2f}"
    log_line = started + ' Started |' + datetime.datetime.now().strftime(
        "%Y/%m/%d %H:%M:%S") + f' Ended | {total_running_time} TotalSecs | Version {current_version} | Hostname {hostname} | OS {os_pataform}' + '\n'
    log_file.write(log_line)
    log_file.close()

    print(out_line)
    print("All Personal Data Warehouse processes have ended! ")
    print(log_line[:-1])
    print(out_line)
    # exit(0)

def monthly_summaries (db_file, in_table, out_table):
    print(f'Generating summaries of all accounting sheets into {out_table} table ... .. .')
    db_conn = sqlite3.connect(db_file)
    sql_statment = f'SELECT * FROM {in_table} ;'
    df_entrada = pd.read_sql(sql_statment, db_conn)

    df_agrupado = df_entrada.groupby(['AnoMes', 'Origem']).agg(
        CREDITO=('Credito', 'sum'),
        DEBITO=('Debito', 'sum')
    ).reset_index()
    df_agrupado['Posição'] = df_agrupado['CREDITO'] - df_agrupado['DEBITO']
    df_agrupado = df_agrupado.sort_values(by=['Origem', 'AnoMes']).reset_index(drop=True)

    df_agrupado_anual = df_entrada.groupby(['Ano', 'Origem']).agg(
        CREDITO=('Credito', 'sum'),
        DEBITO=('Debito', 'sum')
    ).reset_index()
    df_agrupado_anual['Posição'] = df_agrupado_anual['CREDITO'] - df_agrupado_anual['DEBITO']
    df_agrupado_anual = df_agrupado_anual.sort_values(by=['Origem', 'Ano']).reset_index(drop=True)

    df_agrupado_full = df_entrada.groupby('Origem').agg(
        CREDITO=('Credito', 'sum'),
        DEBITO=('Debito', 'sum')
    ).reset_index()
    df_agrupado_full['Posição'] = df_agrupado_full['CREDITO'] - df_agrupado_full['DEBITO']
    df_agrupado_full = df_agrupado_full.sort_values(by='Origem').reset_index(drop=True)

    df_agrupado.to_sql(out_table, db_conn, index=False, if_exists='replace')
    df_agrupado_anual.to_sql(out_table + '_ANUAL', db_conn, index=False, if_exists='replace')
    df_agrupado_full.to_sql(out_table + '_FULL', db_conn, index=False, if_exists='replace')


def data_loader(data_base, types_sheet, general_entries_table, data_origin_col, guindind_sheet, excel_file,
                save_useless, udt):
    print(f"Connecting to SQLite3 Database ... .. .  ")
    conn = sqlite3.connect(data_base)
    work_books = pd.ExcelFile(excel_file)
    print(f"Reading Data from Guindig Sheet :->  {guindind_sheet} ... .. .  ")
    sheets_dataframe = work_books.parse(sheet_name=guindind_sheet)
    table_droppator(conn.cursor(), general_entries_table)
    print("Running Loader of the Sheets into database Tables ... .. .  ")
    first_pass = True
    meses = {1: "01-Janeiro",
             2: "02-Fevereiro",
             3: "03-Março",
             4: "04-Abril",
             5: "05-Maio",
             6: "06-Junho",
             7: "07-Julho",
             8: "08-Agosto",
             9: "09-Setembro",
             10: "10-Outubro",
             11: "11-Novembro",
             12: "12-Dezembro" }

    dias_semana = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }

    for i, infos in sheets_dataframe.iterrows():
        table_to_load = infos.TABLE_NAME
        is_accounting = infos.ACCOUNTING
        is_cleanable = infos.CLEANABLE
        is_loadeable = infos.LOADABLE
        print(f'\033[34m   . .. ... Step: {i + 1:04} ; Table (Sheet) :-> {table_to_load.strip().ljust(25)} ;\033[0m',
              end=' ')
        if 'X' == is_loadeable:
            data_frame = pd.read_excel(excel_file, sheet_name=table_to_load)
            if 'X' == is_accounting:
                # data_frame['TIPO'].replace('', np.nan, inplace=True)
                # data_frame['Data'].replace('', np.nan, inplace=True)
                # 2024.04.03 - improvment for future pandas 3.0
                # Series through chained assignment using an inplace method.
                # The behavior will change in pandas 3.0. This inplace method will never work because the intermediate
                # object on which we are setting values always behaves as a copy.
                data_frame['TIPO'] = data_frame['TIPO'].replace('', np.nan)
                data_frame['Data'] = data_frame['Data'].replace('', np.nan)

                # if 'X' == is_cleanable and not save_useless:  ## ATENÇÃO A ISSO AQUI
                #     # limpa registros com os Tipos Nulos
                #     data_frame.dropna(subset=['TIPO'], inplace=True)
                #     # limpa registros com as Datas Nulas
                #     data_frame.dropna(subset=['Data'], inplace=True)

                general_entries_df = data_frame[["Data", "TIPO", "DESCRICAO", "Credito", "Debito"]].copy()
                general_entries_df[data_origin_col] = table_to_load
                number_lines = len(data_frame)
                # # Convert colunmns "Credito" and "Debito" from str to float
                # general_entries_df['Credito'] = pd.to_numeric(general_entries_df['Credito'], errors='coerce')
                # general_entries_df['Debito'] = pd.to_numeric(general_entries_df['Debito'], errors='coerce')

                # And put the data cleaned into table  lançamentos gerais
                if first_pass:
                    general_entries_df_full = general_entries_df.copy()
                    first_pass = False
                else:
                    general_entries_df_full = pd.concat([general_entries_df_full, general_entries_df],
                                                        ignore_index=True)

            else:
                # Writes only the tables that aren´t Accounting, because it was already loaded on table general_entries_table
                number_lines = data_frame.to_sql(table_to_load, conn, index=False, if_exists="replace")

            print(f'\033[32mLines Created :-> {str(number_lines).rjust(6)} \033[0m')

    print(f'\033[34m   . .. ... Sanitizing DataFrame       :-> {general_entries_table} :\033[0m', end=' ')

    if  not save_useless:  ## ATENÇÃO A ISSO AQUI
        # limpa registros com os Tipos Nulos
        general_entries_df_full.dropna(subset=['TIPO'], inplace=True)
        # limpa registros com as Datas Nulas
        general_entries_df_full.dropna(subset=['Data'], inplace=True)

    # Add new columns with NULL or default values
    general_entries_df_full.insert(1, 'DIA_SEMANA', np.nan)
    general_entries_df_full.insert(6, 'Mes', 'MM')
    general_entries_df_full.insert(7, 'Ano', 'yyyy')
    general_entries_df_full.insert(8, 'MES_EXTENSO', np.nan)
    general_entries_df_full.insert(9, 'AnoMes', 'YYYY/MM')
    dt = general_entries_df_full['Data'].dt

    # fix the data in several columns
    general_entries_df_full = (
        general_entries_df_full
        .assign(
            Credito=pd.to_numeric(general_entries_df_full['Credito'], errors='coerce').round(2).fillna(0),
            Debito=pd.to_numeric(general_entries_df_full['Debito'], errors='coerce').round(2).fillna(0),
            MES_EXTENSO=dt.month.map(meses),
            DIA_SEMANA=dt.dayofweek.map(dias_semana),
            Mes=dt.strftime("%m"),
            Ano=dt.strftime("%Y"),
            AnoMes=dt.strftime("%Y/%m"),
            AnoMesNum=dt.strftime("%Y%m"),   # opcional: AAAAMM numérico
            DESCRICAO = (
                general_entries_df_full['DESCRICAO']
                .str.replace(r"[;,]", "|", regex=True)  # troca vírgula e ponto e vírgula por |
                .str.replace("∴", " .'. ")  # troca caractere especial
                .str.replace("ś","s")
                .str.strip()  # remove espaços extras no início/fim
            )
        )
    )

    # sort the data_frame before persist it on the database'
    general_entries_df_full = general_entries_df_full.sort_values(
        by=general_entries_df_full.columns[0],  # Primeira coluna
        ascending=False,  # Ordenação descendente
        ignore_index=True  # Reindexar após ordenação
    )

    print(f'\033[32mDone !!! \033[0m')

    print(f'\033[34m   . .. ... Writing Dataframe fo Table :-> {general_entries_table} :\033[0m', end=' ')
    general_entries_df_full.to_sql(general_entries_table, conn, index=False, if_exists="replace")
    # Just one commit to Save time. This commit is BEFORE the data_correjeitor
    conn.commit()
    print(f'\033[32mDone !!! \033[0m')

    data_correjeitor(conn.cursor(), types_sheet, general_entries_table, save_useless, udt)
    conn.commit()
    conn.close()

def create_dinamic_reports(sqlite_database, excel_file, din_report_guinding, full_pivot):
    # todo: put some Fancy  output Message
    print('Creating Dynamic Reports for summarized history ... .. . ')
    conn = sqlite3.connect(sqlite_database)
    # with the name of the din_report_guinding , reads the Sheets do be loaded
    data_frame = pd.read_excel(excel_file, sheet_name=din_report_guinding)
    # We have to write this dataframe on db to use the tables further
    number_lines = data_frame.to_sql(din_report_guinding, conn, index=False, if_exists="replace")
    print(f'Dynamic Reports Table Created! Total of Dynamic Reports :-> \033[31m{str(number_lines).rjust(6)}\033[0m ')
    # Now we have to create Single tables of each din report , based on the names of the sheets
    for i, linhas in data_frame.iterrows():
        # now for each din report, we have to read the correspondig excel sheet
        report_table = linhas.DEST_TABLE
        report_xl_sheet = linhas.SHEETY
        report_description = linhas.REPORT_NAME
        print(
            f'\033[34m   . .. ... Step: {i + 1:04} : Creating Dynamic Report Table\033[0m  :-> \033[33m"{report_description}"\033[0m ')
        columns_of_report = pd.read_excel(excel_file, sheet_name=report_xl_sheet)

        # finally, create the table to be used in the future
        # number_lines = columns_of_report.to_sql(report_xl_sheet, conn, index=False, if_exists="replace")
        # print(f'                                        Dynamic Reports :-> {report_table} ')
        # Now, for each dynamic report, read the corresponding Sheet
        df_single_sheet = pd.read_excel(excel_file, sheet_name=report_xl_sheet)
        # here we have to Build de Dynamic table
        base_sql_string = "SELECT "
        sum_tables = " ("
        for j in df_single_sheet.index:
            column_name = df_single_sheet['COLUMN_NAME'][j]
            base_sql_string += "HG.'" + column_name + "',"
            if j > 0:
                sum_tables += "HG.'" + column_name + "'+"

        # At the end of the Loop, fix the Strings
        sum_tables = sum_tables[:-1] + ")"

        base_sql_string = base_sql_string + sum_tables + f' as "Valor Total" FROM {full_pivot} HG; '
        # Now, run the SQL Query to build the Data-frame
        df = pd.read_sql_query(base_sql_string, conn)
        # writes the data-frame into a table on SQLite
        df.to_sql(report_table, conn, if_exists='replace', index=False)

    # Here is the end of the First Loop
    conn.close()

def general_entries_file_exportator(data_base_file, dir_out, file_out, table_name, other_types) :
    connection = sqlite3.connect(data_base_file)
    file_full_path = dir_out + file_out + '.v2'
    print(f"Exporting {file_full_path} to file(s) ")
    sqlStatment = "SELECT substr (LG.DATA, 9,2 )||'-'||substr(LG.DATA,6,2 )||'-' || substr(LG.DATA, 1,4) AS Quando " \
                  ", LG.DIA_SEMANA as 'Dia da Semana' " \
                  ", LG.Tipo as 'Tipo' " \
                  ", LG.DESCRICAO  as 'Descricao/Lancamento' " \
                  ", replace (LG.Credito, '.', ',') as 'Credito' " \
                  ", replace (LG.DEBITO, '.', ',') as 'Debito' " \
                  ", char(39)||cast (mes as text) as 'Mes' " \
                  ", char(39)||cast (ano as text) as 'Ano' " \
                  ", char(39)||MES_EXTENSO as 'Mes(Por Extenso)' " \
                  ", char(39)||cast (AnoMes as text )  as 'Ano/Mes' " \
                  ", LG.ORIGEM  as Origem " \
                  f" FROM {table_name} LG ORDER  BY DATA DESC ; "

    df_out = pd.read_sql(sqlStatment, connection)
    row_count = len(df_out.index)
    df_out.to_csv(file_full_path + '.csv', sep=';', index=False, encoding='cp1252')
    if other_types:
        print(f"              Exporting JSON file(s) ")
        df_out.to_json(file_full_path + '.json', orient='records', lines=True, indent=1, force_ascii=False)
        gzip_compressor(file_full_path + '.json')
        # df_out.to_html(file_full_path + '.html')
        # df_out.to_xml(file_full_path + '.xml', parser = 'lxml', pretty_print=True, xml_declaration=True)
        print(f"              Exporting XML file(s) ")
        dataframe_to_xml(df_out, file_full_path + '.xml')
        gzip_compressor(file_full_path + '.xml')

    print(
        f'File(s) export(s) for table "{table_name}" has been created successfully! Total Lines exported :-> {row_count}')
    connection.close()

# Function that converts any data-frame to XML file
def dataframe_to_xml(df, filename):
    root = ET.Element('data')
    for index, row in df.iterrows():
        item = ET.SubElement(root, 'item')
        # for col_name, col_value in row.iteritems():
        for col_name, col_value in row.items():
            # col_value_escaped = escape_special_chars(str(col_value))
            # ET.SubElement(item, col_name).text = col_value_escaped
            ET.SubElement(item, col_name).text = str(col_value)

    tree = ET.ElementTree(root)
    ET.indent(tree, '   ')
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def transient_data_exportator(sqlite_database, dir_out, out_extension, file_name, transient_data_table, origing_column):
    print('Exporting Transient data into individual Sheelts ... .. .  ')
    file_full_path = dir_out + file_name + '.' + datetime.datetime.now().strftime(
        "%Y%m%d.%H%M%S") + '.' + out_extension
    connection = sqlite3.connect(sqlite_database)
    xlsx_writer = pd.ExcelWriter(file_full_path, engine='xlsxwriter', date_format='yyyy-mm-dd')
    guiding_df = pd.read_sql(f"select distinct {origing_column} from {transient_data_table}", connection)
    conn = connection.cursor()

    for i, linhas in guiding_df.iterrows():
        excel_sheet = f"{linhas.Origem}"
        message = f'   . .. ... Step: {i + 1:04} :-> Exporting Sheet {excel_sheet.ljust(25)} to {file_full_path}'
        sql_statment = f"SELECT * FROM {transient_data_table} where {origing_column} = '{linhas.Origem}' and EXPORT_DATE is null order by 1;"
        df_out = pd.read_sql(sql_statment, connection)
        if len(df_out) > 0:
            print(message)
            df_out.to_excel(xlsx_writer, sheet_name=excel_sheet, index=False)
            conn.execute(
                f"UPDATE {transient_data_table} SET EXPORT_DATE = datetime('now') WHERE {origing_column} = '{linhas.Origem}'; ")
            conn.execute('COMMIT; ')

    connection.close()
    xlsx_writer.close()
    return file_full_path

def xlsx_report_generator(sqlite_database, dir_out, file_name, write_multiple_files, out_extension, entries_table,
                          dynamic_reports, dyn_rep_tab, gera_hist, anual_hist, full_hist, day_prog, splt_pmnt_res,
                          mont_summ):
    # TODO: put the Dynamic Reports statments . How? IDK
    ## PUT here the contagem cumulada call
    totalizador_diario(sqlite_database, entries_table, day_prog)
    print('Exporting Summarized data ... .. .  ')
    connection = sqlite3.connect(sqlite_database)
    file_full_path = dir_out + file_name + '.' + out_extension
    lista_consultas = []
    if write_multiple_files:
        xlsx_writer = pd.ExcelWriter(file_full_path, engine='xlsxwriter', date_format='yyyy-mm-dd')

    if gera_hist:
        lista_consultas.append([
            f"select * from {full_hist} where date(SUBSTR(AnoMes,1,4)||'-'||SUBSTR(AnoMes,6,2)||'-'||'01') >= date('now','-13 month');" \
            , full_hist + "12Meses"])
        lista_consultas.append([f"select * from {full_hist};", f"{full_hist}"])
        lista_consultas.append([f"select * from {anual_hist};", f"{anual_hist}"])
        ###
        lista_consultas.append([
            f"select * from {full_hist}_QTD where date(SUBSTR(AnoMes,1,4)||'-'||SUBSTR(AnoMes,6,2)||'-'||'01') >= date('now','-13 month');" \
            , full_hist + "_QTD12Meses"])
        lista_consultas.append([f"select * from {full_hist}_QTD;", f"{full_hist}_QTD"])
        lista_consultas.append([f"select * from {anual_hist}_QTD;", f"{anual_hist}_QTD"])
        ##

    lista_consultas.append([f"select tipo as Categoria, sum(debito) as Valor , count(1) as QTD from {entries_table}" \
                            " where Data >= date('now','-1 month')  and Data <= date('now', '+1 day') and debito > 0 " \
                            " group by tipo order by 2 desc;", "Ultimos30Dias"])
    # lista_consultas.append(
    #     ["SELECT substr (LG.DATA, 9,2 ) || '/' || substr (LG.DATA, 6,2 ) || '/' || substr(LG.DATA, 1,4) AS Quando " \
    #      ", LG.DIA_SEMANA as 'Dia da Semana' " \
    #      ", LG.Tipo as 'Tipo' " \
    #      ", LG.DESCRICAO  as 'Descricao/Lancamento' " \
    #      ", replace (LG.Credito, '.', ',') as 'Credito' " \
    #      ", replace (LG.DEBITO, '.', ',') as 'Debito' " \
    #      ", char(39)|| substr(LG.DATA, 9,2) as Dia" \
    #      ", char(39)|| mes as 'Mes' " \
    #      # ", char(39)|| cast (mes as text) as 'Mes' " \
    #      # ", char(39)||cast (ano as text) as 'Ano' " \
    #      ", char(39)|| ano as 'Ano' " \
    #      #", char(39)||cast (AnoMes as text )  as 'Ano/Mes' " \
    #      ", LG.MES_EXTENSO as 'Mes Por Extenso' " \
    #      ", char(39)|| AnoMes as 'Ano/Mes' " \
    #      ", LG.ORIGEM  as Origem " \
    #      f" FROM {entries_table} LG ;", entries_table])
    lista_consultas.append(["select Ano || ' - ' || Mes as 'Referência', count(1) as 'Total' " \
                            ", round( cast (count(1) as float)  / ( case Mes when '01' then 31" \
                            " when '02' then 28 when '03' then 31 when '04' then 30 when '05' then 31" \
                            " when '06' then 30 when '07' then 31 when '08' then 31 when '09' then 30" \
                            " when '10' then 31 when '11' then 30 when '12' then 31 end ),2) as 'Por Dia'" \
                            f" from {entries_table} group by  Ano || ' - ' || Mes " \
                            " order by  Ano || ' - ' || Mes desc ;", "Iterações_Mensais"])
    lista_consultas.append(["SELECT DIA_SEMANA, COUNT(1) AS TOTAL " \
                            f" FROM {entries_table} LG " \
                            " WHERE Data >= date('now','-13 month') " \
                            " GROUP BY DIA_SEMANA " \
                            " ORDER BY 2 DESC ;", "Iterações_Semanais_12M"])
    lista_consultas.append(["select dois.AnoMes as Referencia , round(dois.debitos,2) as Débito ," \
                            " round(dois.creditos,2) as Créditos , round(dois.creditos - dois.debitos,2 ) " \
                            " as ""Posição"" from ( SELECT AnoMes , sum (lg.Debito) as debitos , Sum (lg.Credito) " \
                            f" as Creditos FROM {entries_table} LG where LG.TIPO not in " \
                            " ('cartões de Crédito','Transf. Bco') GROUP BY AnoMes order by Ano desc, mes DESC ) dois ;"
                               , "Debitos Mensais"])

    lista_consultas.append([f"SELECT origem, count(1) as Total FROM {entries_table} " \
                            "group by origem ORDER BY Total desc ; ", "Histórico de Uso"])
    lista_consultas.append([f"SELECT * FROM {day_prog} ORDER BY 1 DESC;", "Contagem dia-a-dia"])
    lista_consultas.append([f"SELECT * FROM {splt_pmnt_res} ORDER BY 1 DESC;", "Resumo de Parcelamentos"])
    lista_consultas.append([f"SELECT * FROM {mont_summ} ;", "Resumos_In_out Mensal"])
    lista_consultas.append([f"SELECT * FROM {mont_summ}_ANUAL ;", "Resumos_In_out Anual"])
    lista_consultas.append([f"SELECT * FROM {mont_summ}_full ;", "Resumos_In_out FULL"])
    lista_consultas.append(["select  TIPO ,AnoMes,  sum(Credito) as Creditos, sum (debito)  as Debitos" \
                            f" from {entries_table} lg " \
                            " group by AnoMes , Tipo order by 1,2 ; ", "Resumo Mensal Lancto"])
    lista_consultas.append(["select  TIPO ,Ano,  sum(Credito) as Creditos, sum (debito)  as Debitos" \
                            f" from {entries_table} lg " \
                            " group by Ano , Tipo order by 1,2 ; ", "Resumo Anual Lancto"])

    if gera_hist and dynamic_reports:
        df_dyn = pd.read_sql(f"select * from {dyn_rep_tab}", connection)
        for i, linhas in df_dyn.iterrows():
            lista_consultas.append([f"SELECT * FROM {linhas.DEST_TABLE} ;", f"{linhas.REPORT_NAME}"])

    for k in range(0, len(lista_consultas)):
        consulta = lista_consultas[k]
        sql_statment = consulta[0]
        excel_sheet = consulta[1]
        # print(sql_statment)
        df_out = pd.read_sql(sql_statment, connection)

        if write_multiple_files:
            message = f'\033[34m   . .. ... Step: {k + 1:04} :-> Exporting Sheet {excel_sheet.ljust(27)} \033[33mto {file_full_path}\033[0m'
            df_out.to_excel(xlsx_writer, sheet_name=excel_sheet, index=False)
        else:
            file_full_path = dir_out + excel_sheet + '.v2.' + out_extension
            message = f'   . .. ... Step: {k + 1:04} :-> Exporting {file_full_path} to file(s) '
            df_out.to_excel(file_full_path, sheet_name=excel_sheet, index=False, date_format='DD/MM/YYYY')

        print(message)

    connection.close()
    if write_multiple_files:
        xlsx_writer.close()


def data_correjeitor(conexao, types_sheet, entries_table, save_useless, useless_table):
    print(f'Normalizing data on {entries_table} Table ...')
    cursor = conexao
    lista_acoes = []
    if save_useless:
        print(f'   . .. ... Saving discated Data')
        table_droppator(cursor, useless_table)
        lista_acoes.append((
            f"create table {useless_table} as select * from {entries_table} where (data is null or tipo is null); ",
            "Saving Useless"))
        lista_acoes.append((f"delete from {entries_table} where (data is null or tipo is null);", "Deleting Useless"))

    lista_acoes.append(
        (f"Delete from {types_sheet} WHERE ( Código IS NULL or Descrição IS NULL) ;", "Deleting NULL info"))
    lista_acoes.append(('DELETE FROM Parcelamentos WHERE 1 = 1 AND (DATA IS NULL OR "Tipo Lançamento" is null) ;',
                        "Deleting Parcelamentos"))
    # lista_acoes.append((f'create index SHAWASKA on {entries_table}  (DATA, TIPO, DESCRICAO) ',"(Re)creating Index"))
    lista_acoes.append((f'DROP VIEW IF EXISTS Origens; ', "Dropping View"))
    lista_acoes.append((
                       f"create view Origens as select TABLE_NAME as nome from GUIDING gd where gd.LOADABLE = 'X' AND GD.ACCOUNTING = 'X';",
                       "Creating View"))

    for i in range(0, len(lista_acoes)):
        sql_string = lista_acoes[i][0]
        action_desc = lista_acoes[i][1].ljust(25)
        print(f'\033[34m   . .. ... Step: {i + 1:04} :-> {action_desc} ;\033[0m', end=' ')
        cursor.execute(sql_string)
        print(f'\033[31mLines Affected: {str(cursor.rowcount).rjust(5)}\033[0m')

def table_droppator(conexao, table_name):
    cursor = conexao
    cursor.execute("DROP TABLE IF EXISTS " + table_name)
    print(f"Table {table_name} dropped... ")


def create_pivot_history(data_base_file, types_table, entries_table, out_table_General, out_table_Anual):
    print('Creating pivot Tables ... .. . ')
    connection = sqlite3.connect(data_base_file)

    sql_statment_types = f'SELECT Descrição as TIPO FROM {types_table} ;'
    sql_statment_summary = f'SELECT * FROM {entries_table} ;'

    df_summary = pd.read_sql(sql_statment_summary, connection)
    df_types = pd.read_sql(sql_statment_types, connection)

    print('                      ... .. . to Monthly Values to summarized in history ... .. .')
    pivot_full = df_summary.pivot_table(index='AnoMes', columns='TIPO', values='Debito', aggfunc='sum').fillna(0)
    pivot_full = pivot_full[df_types['TIPO']]
    pivot_full = pivot_full.reset_index()
    pivot_full.to_sql(out_table_General, connection, index=False, if_exists="replace")

    print('                      ... .. . to Monthly total to summarized in history ... .. .')
    pivot_full = df_summary.pivot_table(index='AnoMes', columns='TIPO', values='Debito', aggfunc='count').fillna(0)
    pivot_full = pivot_full[df_types['TIPO']]
    pivot_full = pivot_full.reset_index()
    pivot_full.to_sql(out_table_General + '_QTD', connection, index=False, if_exists="replace")

    print('                      ... .. . to Anual Values to summarized in history ... .. .')
    pivot_anual = df_summary.pivot_table(index='Ano', columns='TIPO', values='Debito', aggfunc='sum').fillna(0)
    pivot_anual = pivot_anual[df_types['TIPO']]
    pivot_anual = pivot_anual.reset_index()
    pivot_anual.to_sql(out_table_Anual, connection, index=False, if_exists="replace")

    print('                      ... .. . to Anual total summarized in history ... .. .')
    pivot_anual = df_summary.pivot_table(index='Ano', columns='TIPO', values='Debito', aggfunc='count').fillna(0)
    pivot_anual = pivot_anual[df_types['TIPO']]
    pivot_anual = pivot_anual.reset_index()
    pivot_anual.to_sql(out_table_Anual + '_QTD', connection, index=False, if_exists="replace")

    connection.commit()


def parallel_df(db_file, xls_file, config_dict, general_out_table, index):
    db_connection = sqlite3.connect(db_file)
    tmp_table_name = config_dict['table_to_load']
    print(f'   . .. ... .... Begin of Thread Number :-> {index}  ; Table/Sheet Name :-> {tmp_table_name} ')
    data_frame = pd.read_excel(xls_file, sheet_name=config_dict['table_to_load'])
    if 'X' == config_dict['isAccounting'] and 'X' == config_dict['isCleanable']:
        # delete records with null 'TIPO'
        data_frame['TIPO'].replace('', np.nan, inplace=True)
        data_frame.dropna(subset=['TIPO'], inplace=True)
        # delete records with null DATA column
        data_frame['Data'].replace('', np.nan, inplace=True)
        data_frame.dropna(subset=['Data'], inplace=True)
        general_entries_df = data_frame[["Data", "TIPO", "DESCRICAO", "Credito", "Debito"]].copy()
        general_entries_df.insert(1, 'DIA_SEMANA', np.nan)
        general_entries_df['Mes'] = 'MM'
        general_entries_df['Ano'] = 'YYYY'
        general_entries_df['AnoMes'] = 'YYYY/MM'
        general_entries_df['Origem'] = config_dict['table_to_load']
        # Ja joga os dados limpos na lançamentos gerais
        general_entries_df.to_sql(general_out_table, db_connection, index=False, if_exists="append")

    # grava a tabela (UNITÁRIA) do data_frame do BD
    data_frame.to_sql(config_dict['table_to_load'], db_connection, index=False, if_exists="replace")
    db_connection.commit()
    db_connection.close()
    print(f'   . .. ... .... End of Thread Number :-> {index}  ; Table/Sheet Name :-> {tmp_table_name} ')

# def data_loader_parallel(data_base, general_entries_table, guindind_sheet, excel_file):
def data_loader_parallel(data_base, types_sheet, general_entries_table, guindind_sheet, excel_file, save_useless, udt):
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
        print(f'   . .. ... Step:->  {i + 1:04} ; Table (Sheet) :-> "{tmp_table_name}"')
        if 'X' == dict_config['isLoadeable']:
            # thread = threading.Thread(target=parallel_df(conn, excel_File, dict_config, General_Entries_table, i + 1))
            thread = threading.Thread(target=parallel_df,
                                      args=(data_base, excel_file, dict_config, general_entries_table, i + 1))
            jobs.append(thread)

    print(f'   . .. ... Starting Multi-Threaging processing')
    for m in jobs:
        m.start()

    print(f'   . .. ... Waiting for Threads to End ')
    # Ensure all  the threads have finished
    for index, tread in enumerate(jobs):
        print(f'   ... .. . Index Of :-> {index}')
        thread.join()

    print(f'   . .. ... All threads has ended ')
    data_correjeitor(conn.cursor(), types_sheet, general_entries_table, save_useless, udt)
    print(f'   . .. ... Data-Loader Done !!! !! ! ')
    conn.commit()
    conn.close()
    # connection.close()

def gzip_compressor(arquivo_origem):
    arquivo_destino = arquivo_origem + '.gz'
    print(f'creating compressed file {arquivo_destino}')
    with open(arquivo_origem, 'rb') as f_in:
        with gzip.open(arquivo_destino, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Excluindo o arquivo original após a compactação
    os.remove(arquivo_origem)


def totalizador_diario(database_file, in_table, out_table):
    print("Totaling the Daily Amount of data ... .. .")
    conn = sqlite3.connect(database_file)
    df = pd.read_sql_query(f"select * from {in_table}", conn)
    df_contagem = df.groupby('Data').size().reset_index(name='Contagem')
    df_contagem['Contagem Acumulada'] = df_contagem['Contagem'].cumsum()
    df_contagem = df_contagem[['Data', 'Contagem Acumulada']]
    number_lines = df_contagem.to_sql(out_table, conn, index=False, if_exists="replace")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    input_param_file = ""

    if len(sys.argv) == 2:
        input_param_file = sys.argv[1]

    main(input_param_file)

# EOP
