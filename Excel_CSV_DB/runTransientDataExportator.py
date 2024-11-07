from  PersonalDataWareHouse import transient_data_exportator as TDE
import configparser
import os, platform, sys

def extrair_dados (db_input):
    pass
    current_version = "9.7.0"
    config = configparser.ConfigParser()
    config_file = 'PersonalDataWareHouse.cfg'
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

        dir_file_out = config['DIRECTORIES']['DIR_OUT']
        out_type = config['FILE_TYPES']['TYPE_OUT']
        transient_data_file = config['FILE_TYPES']['TRANSIENT_DATA_FILE']
        transient_data_table = config['SETTINGS']['TRANSIENT_DATA_TABLE']
        origem_dados = config['SETTINGS']['TRANSIENT_DATA_COLUMN']

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

    TDE(db_input, dir_file_out, out_type, transient_data_file, transient_data_table,  origem_dados )

if __name__ == '__main__':
    input_param_file = ""

    if len(sys.argv) == 2:
        input_param_file = sys.argv[1]
    else:
        print('ERROR - FATAL - FAIL ')
        print('Input database file name is Missing or not found !!!!!')
        exit(1) 

    extrair_dados (input_param_file)

# EOP