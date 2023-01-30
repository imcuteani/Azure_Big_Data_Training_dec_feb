# connection with Azure SQL db/ on-premise SQL db 

import pymssql          # use it for connecting to Azure SQL db
import pyodbc           # on-premise SQL server db

server = '<SQL_server_name>'
database = 'AdventureWorksLT2019'
username = '<SQL_auth_user>'
password = '<SQL_auth_pwd>'
conn = pyodbc.connect(driver='{SQL Server}',server=server, user=username, password=password, database=database)

# define the SQL Cursor object 
cursor = conn.cursor()
cursor.execute('SELECT c.CustomerID, c.CompanyName, COUNT(sh.SalesOrderID) AS OrderCount FROM SalesLT.Customer as c LEFT OUTER JOIN SalesLT.SalesOrderHeader as sh ON c.CustomerID = sh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')
row = cursor.fetchone()
while row:
    result_1 = (str(row[0]))
    result_2 = (row[1])
    result_3 = (str(row[2]))
    print(result_1)
    print(result_2)
    print(result_3)
    newresult = (str(row[0]), "|", (row[1]), "|", str(row[2]))
    print(newresult)
    row = cursor.fetchone()

