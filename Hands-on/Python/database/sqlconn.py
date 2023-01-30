# connect to SQL Server database 

# there are two libraries available to connect to the backend SQL server database 

# 1. pyodbc 
# 2. pymssql 

import pyodbc 

# passing over parameters for SQL server database 
server = '<SQL_server_name>'
database = 'AdventureWorksLT2019'
username = '<sql_auth_username>'
password = '<sql_auth_password>'

# ENCRYPT defaults to yes in ODBC driver, it's good to specify ENCRYPT=yes on the client side to avoid MITM Attacks
cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=database, UID = username, PWD = password)
cursor = cnxn.cursor()

# Run the SQL query 

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()




