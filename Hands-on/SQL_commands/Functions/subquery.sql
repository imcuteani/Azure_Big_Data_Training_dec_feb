-- Subquery in SQL Server -- 

-- IN SQL , the subquery refers as a query defined in another query. 
-- A subquery is a query which is embedded in WHERE clause of another SQL query. 

-- you can place the subquery in a number of SQL clauses - 
-- WHERE clause
-- HAVING clause
-- FROM clause 
-- Subqueries can be used with SELECT, UPDATE, INSERT, DELETE statements
-- it can be used with operators =, >=, <= and LIKE operator etc.
-- subquery means a query within another query. Where the outer query is called main query 
-- and inner query is called subquery. 

use AdventureWorksLT2019; 

select SalesOrderID, 
UnitPrice,
ModifiedDate,
ProductID
FROM 
SalesLT.SalesOrderDetail
WHERE 
ProductID IN (select ProductID
from SalesLT.Product 
WHERE Color = 'Red')
ORDER BY 
ModifiedDate DESC; 

-- if though the subquery returns a NULL value, the EXISTS() operator in SQL Server is still evaluates to the TRUE

select 
CustomerID,
FirstName,
LastName
FROM
SalesLT.Customer
WHERE 
EXISTS(SELECT NULL) -- EXISTS operator evaluates TRUE since SELECT query within the subquery returns NULL 
ORDER BY FirstName,
LastName