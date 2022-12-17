-- Choose Function 

-- it's available in tSQL to return the item at the specified index from the list of values 

-- an item can also be retrieved as the specific index position from the list 

-- CHOOSE(index, value[1], value[2]... value[n])

-- return of items depends on the index 
-- depends on the items, helps to pick the item as per the index specified


use AdventureWorks2016;

-- retrieve the distinct names of the person, date and specific month in SQL query through CHOOSE function

select 
DISTINCT(FirstName + ' '+ LastName) AS NAME 
, DATEPART(DD, ModifiedDate) AS [Date]
, CHOOSE(DATEPART(MM, ModifiedDate), 'January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December')[Month]
, DATEPART(YYYY, ModifiedDate) AS [YEAR]
FROM Person.Person 
ORDER BY Name ASC 

select ModifiedDate from Person.Person;

select OrderQty from Sales.SalesOrderDetail;

-- IIF function in SQL Server 

-- IIF is a logical function in TSQL and defines the one of the two values depending upon the condition met, 
-- whether the boolean expression returned to be TRUE or FALSE 

SELECT IIF(500<1000, 'YES', 'NO')

-- IIF function returns true if a condition is TRUE, or another value is shown if the condition is false 

-- IIF(condition, value_if_true, value_if_false)

select SalesOrderID, OrderQty, IIF(OrderQty>5, 'More', 'Less')
FROM Sales.SalesOrderDetail; 
