import configparser
config = configparser.ConfigParser()

try:
    print('Lendo arquivo de configuracao...')

    with open('config.ini') as cfg:
        config.read_file(cfg)


    DIR_FILE_IN = config['DIRETORIOS']['entrada']
    DIR_FILE_OUT  = config['DIRETORIOS']['saida']

    SPLITTER = config.getint('settings','PARALLELS')

    IN_TYPE = config['TIPO_ARQUIVOS']['ENTRADA']
    OUT_TYPE = config['TIPO_ARQUIVOS']['SAIDA']

    NOVO01 = config.getboolean('settings','MULTITHREADING')
    NOVO02 = config.getboolean('settings', 'SOBRESCREVER_DB')
    #NOVO02 = config.getboolean('settings', 'SelfDestruction')

    print('================================================================')
    print(f' Dir. Entrada            :-> {DIR_FILE_IN}')
    print(f' Dir. Saida              :-> {DIR_FILE_OUT}')
    print(f' Tipo de entradas        :-> {IN_TYPE}')
    print(f' Tipo de Saidas          :-> {OUT_TYPE}')
    print(f' Quantidade Paralelos    :-> {SPLITTER} ')
    print(f' Multi-Threading Process :-> {NOVO01} ')
    print(f' SobrescreverDB File     :-> {NOVO02} ')



except FileNotFoundError:
    print("Arquivo de configuracao nao encontrado!")
except configparser.Error as e:
    print(e)
    exit(1)
except Exception as e:
    print(e)
    exit(1)

