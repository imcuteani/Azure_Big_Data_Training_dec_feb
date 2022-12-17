-- SQL Server Views -- 

-- A view in SQL Server is mainly a SELECT statement that has been given a name 
-- and stored in the database. 
-- The main advantage of a view is that once it's created, it acts like a table, 
-- any other SELECT statements that you wish to write. 

-- syntax for creation of view 

-- CREATE VIEW [schema_name.] view_name [(col_name...)]
-- [WITH <view_attribute> [...n]]
-- AS SELECT_statement
-- [WITH_CHECK_Option]

-- Although view is stored name for a SELECT statement, the SELECT statement defined
-- for the view can reference tables, other views , and functions. 
-- The select statement in the view 

-- a) cant contain the COMPUTE or COMPUTE by Clause 
-- b) cant use INTO keyword
-- c) cant use OPTION clause 
-- d) cant reference a temp table or variable of any type
-- e) cant contain an ORDER BY clause unless a TOP operator is specified. 


use AdventureWorksLT2019;
GO

--drop view SalesLT.CustomerOrdersByAddress
--GO

CREATE VIEW SalesLT.CustomerOrderByAddress
AS 
SELECT CASE WHEN a.CompanyName IS NOT NULL THEN a.CompanyName
ELSE a.FirstName + ' ' + a.LastName END CustomerName,
b.AddressID, b.AddressType, b.ModifiedDate, b.CustomerID, c.OrderDate, c.TotalDue,
c.ShipDate 
FROM SalesLT.Customer as a INNER JOIN SalesLT.CustomerAddress as b 
ON a.CustomerID = b.CustomerID
INNER JOIN SalesLT.SalesOrderHeader c ON a.CustomerID = c.CustomerID
GO


-- Query the View -- 

select * from SalesLT.CustomerOrderByAddress
GO 

-- Drop / delete the view -- 

DROP VIEW SalesLT.vProductAndDescription
GO 


