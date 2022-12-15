-- Group BY Clause in SQL Server 

-- GROUP BY clause allows to arrange the rows for a query of groups. These groups 
-- are determined by the columns specified in the GROUP BY clause

use "AdventureWorksLT2019"
go

-- select top 10 customerID from SalesLT.Customer 

-- The IN operator is a logical operator that allows to test whether a specified value matches with any values in a list 

select 
CustomerID, 
SalesPerson, 
CompanyName,
Phone,
ModifiedDate
FROM SalesLT.Customer
WHERE CustomerID IN (12, 29, 30, 40)
GROUP BY 
CustomerID, 
SalesPerson,
CompanyName,
Phone,
ModifiedDate
ORDER BY 
CustomerID