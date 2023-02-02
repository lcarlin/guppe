# -*- coding: ansi -*-
# import sqlite3
import pandas as pd
import mysql.connector

# cbanco de dados.
#con = sqlite3.connect('Lancamentos_Gerais.FULL.db')

# entrada - data Frame
df = pd.read_csv('Lancamentos_Gerais.FULL.csv')
# print(df)

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        print("Subindo dados na tabelas")
        df.to_sql(df, connection, index=False, if_exists="replace")
        cursor.close()
        connection.close()
        print("MySQL connection is closed")




#con.commit()
#con.close()