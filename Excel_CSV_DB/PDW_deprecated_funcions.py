# 2025-26-11
import datetime, sqlite3
import pandas as pd
#######################################################################################################
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
            # AnoMesNum=dt.strftime("%Y%m"),   # opcional: AAAAMM numérico
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

#######################################################################################################
def transient_data_exportator(sqlite_database, dir_out, out_extension, file_name, transient_data_table, origing_column):
    print('Exporting Transient data into individual Sheelts ... .. .  ')
    file_full_path = dir_out + file_name + '.' + datetime.datetime.now().strftime(
        "%Y%m%d.%H%M%S") + '.' + out_extension
    connection = sqlite3.connect(sqlite_database)
    xlsx_writer = pd.ExcelWriter(file_full_path, engine='xlsxwriter', date_format='yyyy-mm-dd')
    guiding_df = pd.read_sql(f"select distinct {origing_column} from {transient_data_table} where EXPORT_DATE is null", connection)
    conn = connection.cursor()

    if not guiding_df.empty:
        for i, linhas in guiding_df.iterrows():
            excel_sheet = f"{linhas.Origem}"
            sql_statment = f"SELECT * FROM {transient_data_table} where {origing_column} = '{linhas.Origem}' and EXPORT_DATE is null order by 1;"
            df_out = pd.read_sql(sql_statment, connection)
            total_linhas = len(df_out)
            if total_linhas > 0:
                message = f'   . .. ... Step: {i + 1:04} :-> Exporting {str(total_linhas).rjust(8)} lines to Sheet {excel_sheet.ljust(25)} to {file_full_path}'
                print(message)
                df_out.to_excel(xlsx_writer, sheet_name=excel_sheet, index=False)
                conn.execute(
                    f"UPDATE {transient_data_table} SET EXPORT_DATE = datetime('now') WHERE {origing_column} = '{linhas.Origem}'; ")
                conn.execute('COMMIT; ')
            else:
                print(f"No data found for {excel_sheet}")

        connection.close()
        xlsx_writer.close()

    else:
        print("Nothing to do! ")

    return file_full_path

#######################################################################################################
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

#######################################################################################################
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

#######################################################################################################
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
#######################################################################################################

def escape_special_chars(text):
    return saxutils.escape(text, entities={
        "'": "&apos;",
        '"': "&quot;",
        '>': "&gt;",
        '<': "&lt;",
        '&': "&amp;",
        'á': "&aacute;",
        'à': "&agrave;",
        'ã': "&atilde;",
        'â': "&acirc;",
        'é': "&eacute;",
        'è': "&egrave;",
        'ê': "&ecirc;",
        'í': "&iacute;",
        'ì': "&igrave;",
        'ó': "&oacute;",
        'ò': "&ograve;",
        'õ': "&otilde;",
        'ô': "&ocirc;",
        'ú': "&uacute;",
        'ù': "&ugrave;",
        'û': "&ucirc;",
        'ç': "&ccedil;",
        'Á': "&Aacute;",
        'À': "&Agrave;",
        'Ã': "&Atilde;",
        'Â': "&Acirc;",
        'É': "&Eacute;",
        'È': "&Egrave;",
        'Ê': "&Ecirc;",
        'Í': "&Iacute;",
        'Ì': "&Igrave;",
        'Ó': "&Oacute;",
        'Ò': "&Ograve;",
        'Õ': "&Otilde;",
        'Ô': "&Ocirc;",
        'Ú': "&Uacute;",
        'Ù': "&Ugrave;",
        'Û': "&Ucirc;",
        'Ç': "&Ccedil;",
    })

#######################################################################################################

def data_verificator(general_entries_table, conexao ):
    print(f'Verifying the Integrity and quality of data loaded into {general_entries_table} ... .. .')
    conta_erro = 0
    lista_acoes = []
    lista_acoes.append(['Data','Validação de datas', '[a-z][A-Z]' ])
    lista_acoes.append(['Debito','Validação de Campo "Debitos"', '[a-z][A-Z]'])
    lista_acoes.append(['Credito', 'Validação de Campo "Creditos"', '[a-z][A-Z]'])
    main_df = pd.read_sql(f'select * from {general_entries_table}', conexao)
    return True

    for i in range(0, len(lista_acoes)):
        field = lista_acoes[i][0]
        action = lista_acoes[i][1] # Action
        regex = lista_acoes[i][2]
        # print('------------ THIS IS A DEBUG  ')
        # print(f'field  -> {field}')
        # print(f'action -> {action}')
        # print(f'regex  -> {regex}')

        # print('------------ THIS IS A DEBUG  ')
        print(f'\033[34m   . .. ... Step: {i + 1:04} : {action} : \033[0m', end=' ')
        net_df = main_df[~main_df[f"{field}"].str.contains(regex, regex=True, na=True)]
        if len (net_df) > 0:
            conta_erro+=1
            print(f'\033[31m FAIL - ERROR :\033[0m')
            print('=======================================================================================')
            print(net_df)
            print('=======================================================================================')
        else:
            print(f'\033[32m OK - SUCCESS; \033[0m')

    if conta_erro == 0:
        return True
    else:
        return False
#######################################################################################################

def create_pivot_history_anual(data_base_file, types_table, entries_table, out_table):
    print('Creating pivot Table for Anual summarized history ... .. . ')
    connection = sqlite3.connect(data_base_file)
    ref_anterior = 'YYYY/MM'
    sql_statment_types = f'SELECT Código as COD, Descrição as DESC FROM {types_table} ;'
    sql_statment_summary = f'select Ano as Referencia, TIPO, sum(Debito) as DEBITOS FROM {entries_table} ' \
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


def create_pivot_history_full(data_base_file, types_table, entries_table, out_table):
    print('Creating pivot Table for summarized history ... .. . ')
    connection = sqlite3.connect(data_base_file)
    ref_anterior = 'YYYY/MM'
    sql_statment_types = f'SELECT Código as COD, Descrição as DESC FROM {types_table} ;'
    sql_statment_summary = f'select AnoMes as Referencia, TIPO, sum(Debito) as DEBITOS FROM {entries_table} ' \
                           ' GROUP BY AnoMes, TIPO order by Ano, Mes, TIPO desc ;'
    df_types = pd.read_sql(sql_statment_types, connection)
    df_summary = pd.read_sql(sql_statment_summary, connection)
    dict_hist_base = {'Referencia': '9999/99'}
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
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################