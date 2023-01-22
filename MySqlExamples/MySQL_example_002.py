# https://www.hostinger.com/tutorials/mysql/how-create-mysql-user-and-grant-permissions-command-line
# https://pynative.com/python-mysql-database-connection/
# https://pypi.org/project/sqlite3-to-mysql/
# pip install sqlite3-to-mysql
# sqlite3mysql --help
# sqlite3mysql -f "G:\Meu Drive\PDW\PDW.db" -d PDW -u xcprd01 -p -h localhost -P 3306 -E

import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")