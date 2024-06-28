import datetime
import os, platform, sys
import time
import shutil


def main(old_log_file):
    new_log_file = old_log_file + ".new"
    lista_nova = []
    try:
        print('Reading configuration file ... .. .')
        with open(old_log_file) as log_antigo:
            for linha in log_antigo:
                old_start = linha.split('|')[0]
                old_end = linha.split('|')[2]
                restantes = "|".join(linha.split("|")[4:])  # linha.split("|")[4:]
                print('-------------------------------------------------------')
                print(f'Old Start :-> {old_start}')
                print(f'Old End   :-> {old_end}')
                old_srt_dt = old_start.split(" ")[0]
                old_srt_tm = old_start.split(" ")[1]
                new_str_tm = old_srt_dt.split("/")[2] + "/" + old_srt_dt.split("/")[1] + "/" + old_srt_dt.split("/")[0]

                old_end_dt = old_end.split(" ")[0]
                old_end_tm = old_end.split(" ")[1]
                new_end_tm = old_end_dt.split("/")[2] + "/" + old_end_dt.split("/")[1] + "/" + old_end_dt.split("/")[0]

                saida = new_str_tm + " " + old_srt_tm + "| Started|" + new_end_tm + " " + old_end_tm + "| Ended|" + restantes[
                                                                                                                    :-1]
                lista_nova.append(saida)

        with open(new_log_file, 'w') as out_file:
            linhas = [linha + '\n' for linha in lista_nova]
            out_file.writelines(linhas)

    except Exception as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    input_param_file = ""
    if len(sys.argv) == 2:
        input_param_file = sys.argv[1]
    else:
        print("ERROR - FATAL - FAIL - WARNING ")
        print("Faltou o nome do arquivo de entrada")
        exit(1)

    main(input_param_file)
