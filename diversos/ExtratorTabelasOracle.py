import datetime
import configparser
import cx_Oracle
import csv

config = configparser.ConfigParser()

try:

    print('Lendo arquivo de configuracao...')

    with open('conf/config.ini') as f:
        config.read_file(f)

    user = config['oracle']['user']
    passwd = config['oracle']['password']
    db = config['oracle']['db']

    print('Db configuration:')
    print(f'User: {user}')
    print(f'Password: {passwd}')
    print(f'Database: {db}')

    print('Conectando com o banco...')
    connection = cx_Oracle.connect(user, passwd, db)
    cursor = connection.cursor()

    try:
        print("Apagando tabela temporaria")
        cursor.execute("drop table rel_teste")
        print(" Tabela removida com sucesso.")
    except cx_Oracle.Error as e:
        print(" Tabela rel_teste nao existe...")

    try:
        print("Iniciando a criacao da tabela rel_teste")
        cursor.execute(config['sql']['criaTabela'])
        print(" Tabela criada com sucesso")

        print("Preenchendo registros...")
        cursor.execute("""select * from rel_teste""")
        rows = cursor.fetchall()

        # Continue only if there are rows returned.
        if rows:
            # New empty list called 'result'. This will be written to a file.
            result = list()

            # The row name is the first entry for each entity in the description tuple.
            column_names = list()
            for i in cursor.description:
                column_names.append(i[0])

            result.append(column_names)
            for row in rows:
                result.append(row)

            # Write result to file.
            strDate = datetime.datetime.now()

            with open("rel_infotim_"+strDate.strftime("%Y%m%H%M%S")+".csv", 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in result:
                    csvwriter.writerow(row)
        else:
            exit("No rows found for query: {}".format(config['sql']['criaTabela']))
    except Exception as e:
        print("Erro ao criar tabela e extrair registros:\n", e)

    print("Fim do processamento")

except FileNotFoundError:
    print("Arquivo de configuracao nao encontrado!")
except configparser.Error as e:
    print(e)
    exit(1)
except Exception as e:
    print(e)
    exit(1)