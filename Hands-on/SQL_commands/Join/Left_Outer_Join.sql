-- Left Outer Join --- 

-- A SQL Left outer join will return all the records from the left side table in the join clause.
-- regardless of the matching records in the right table. 
-- the left SQL outer join includes the rows where the condition is met including
-- all of the rows from the table on the left where the condition is not met are defined. 

-- Fields from the right table with no match will be displayed as NULL values


-- more than two tables can be joined in one single select statement
-- more than one join type can be used in a single select statement 

-- For left side table, both of the matching and non-matching records will be retrieved 
-- whereas for right side table, only the matching records will be retrieved, non-matching records will be displayed as NULL values

use AdventureWorksLT2019;

select a.ProductID, a.Name, b.SalesOrderID 
FROM 
SalesLT.Product a 
LEFT OUTER JOIN 
SalesLT.SalesOrderDetail b 
ON a.ProductID = b.ProductID
WHERE a.Color = 'Red'
ORDER BY 1; 

use AdventureWorks2016;

select a.ProductID,
a.Name,
a.ListPrice,
b.StandardPrice,
b.OnOrderQty
FROM 
Production.Product a LEFT OUTER JOIN 
Purchasing.ProductVendor b 
ON a.ProductID = a.ProductID

