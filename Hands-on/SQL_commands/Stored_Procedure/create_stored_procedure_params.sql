--- SQL Server Stored procedure with Parameters using Wildcard 

-- we can use '%' wildcard parameters 

use AdventureWorks2016
GO 

CREATE PROCEDURE dbo.uspGetAddressWildCard @City NVARCHAR(50)
AS 
SELECT * 
FROM Person.Address
WHERE City LIKE @City + '%'
GO 

