# https://www.hostinger.com/tutorials/mysql/how-create-mysql-user-and-grant-permissions-command-line
# https://pynative.com/python-mysql-database-connection/

import mysql.connector
from mysql.connector import Error

try:
    connection_config_dict = {
        'user': 'pynative',
        'password': 'pynative@#29',
        'host': '127.0.0.1',
        'database': 'Electronics',
        'raise_on_warnings': True,
        'use_pure': False,
        'autocommit': True,
        'pool_size': 5
    }
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")