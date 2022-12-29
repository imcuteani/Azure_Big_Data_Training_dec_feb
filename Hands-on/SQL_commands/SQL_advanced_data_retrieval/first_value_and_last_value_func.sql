-- First Value Function and Last Value function in TSQL -- 

-- the First_Value() returns the value of the specified expression based on the first row of the table/relation
-- the Last_value() returns the value of the expression with the last row of the table/relation 

use AdventureWorks2016

select SalesOrderID, 
ShipDate, 
SalesOrderNumber,
TotalDue,
First_Value(TotalDue) OVER (ORDER BY TotalDue) firstDue,
Last_value(TotalDue) OVER (ORDER BY TotalDue) lastDue
FROM Sales.SalesOrderHeader;