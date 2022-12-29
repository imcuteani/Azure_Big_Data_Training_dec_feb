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

-- Invoke the Stored procedure with Wildcard parameter

use AdventureWorks2016
GO 

EXEC dbo.uspGetAddressWildCard @City = 'New' 
GO

-- Stored procedure with multiple parameters 

CREATE PROCEDURE dbo.uspGetMultiParam @City NVARCHAR(50) = NULL,
 @AddressLine1 NVARCHAR(60) = NULL
AS 
SELECT * 
FROM Person.Address 
WHERE City = ISNULL(@City, City)
AND AddressLine1 LIKE '%' + ISNULL(@AddressLine1, AddressLine1) + '%'
GO

-- execute/ call the stored procedure 

EXEC dbo.uspGetMultiParam @City = 'Calgary', @AddressLine1 = 'A'
GO 

EXEC dbo.uspGetMultiParam @City = 'Calgary', @AddressLine1 = 'S'
GO 


