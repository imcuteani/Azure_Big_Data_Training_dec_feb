-- Stored Procedure in SQL Server -- 

-- SQL Server stored procedure is a batch of statements grouped as logical unit and stored 
-- in the database. 
-- The stored procedure in SQL Server accepts the parameters and executes the T-SQL 
-- statements in the procedure, returns the result set if any. 

-- Benefits of using a stored procedure 

-- 1. it can be easily modified -- we can easily modify the code inside the stored procedure
-- without the need to restart or deploying the app. If the tSQL queries are written in the app 
-- if we need to change the logic, we must change the code in the app and deploy it. 

---2. Reduced network traffic - when we use stored procedure instead of writing tSQL queries at the app level, only the procedure name is passed over the network. 
-- instead of while tsql code. 

---3. Reusable -- stored procedure can executed by multiple users or multiple clients without the need the writing
-- code again and gain

-- 4. Performance -- the SQL server stored procedures when executed for the first time, creates a plan and stored it in the buffer pool 
-- so that the plan can be reused when it executes the next time

-- variables provides a way to manipulate, store and pass the data within a stored procedure. 

-- local variable
-- global variable 

-- local variables are designated by @symbol, create, read, update or deleted
-- global variables are designated by @@symbol - you cant perform create, or write to global variables. 

-- @@ERROR -- Error code from the last statement executed in Stored procedure 
-- @@IDENTITY -- value of the last identity value inserted in the SQL table within the connection
--@@ROWCOUNT -- the number of rows affected by the last executed SQL statement
-- @@TRANCOUNT -- the number of open SQL transactions with the connection
--@@VERSION -- the version of SQL Server (SQL Server 2019- v15, SQL Server 2017 - v14)

use AdventureWorks2016
GO 

DECLARE @City NVARCHAR(50)
SET @City = 'New York'

SELECT * 
FROM Person.Address
WHERE City = @City 
GO 

-- Create a Stored Procedure using a Parameter -- 

use AdventureWorks2016
GO 

-- Delete/ Drop the Stored Procedure

-- DROP PROCEDURE dbo.uspGetAddress
--GO 

CREATE PROCEDURE dbo.uspGetNewAddress @City NVARCHAR(50)
AS 
SELECT * 
FROM Person.Address
WHERE City = @City
GO 

-- Execute / call the Stored Procedure (passing the parameter value at runtime)

EXEC dbo.uspGetNewAddress @City = 'New York'
GO 

EXEC dbo.uspGetNewAddress @City = 'Sydney'
GO 

