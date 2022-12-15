-- ORDER BY clause -- 

use "AdventureWorksLT2019"
GO 

select FirstName, 
MiddleName,
LastName,
CompanyName, 
SalesPerson,
EmailAddress,
Phone
FROM SalesLT.Customer
ORDER BY FirstName
GO 

-- using numbers in ORDER BY clause to sort the result set based on ordinal positions of columns which appear in the list


-- SQL server allows ordering of columns based on number as specified in column order (here, 1= FirstName, 2 = MiddleName etc.)

select FirstName, 
MiddleName, 
LastName,
CompanyName,
SalesPerson,
EmailAddress,
Phone 
FROM SalesLT.Customer
ORDER BY 1 DESC
GO

-- specify ascending and descending order in the same query 

select FirstName, 
MiddleName, 
LastName,
CompanyName,
SalesPerson,
EmailAddress,
Phone
FROM 
SalesLT.Customer
ORDER BY FirstName ASC,
LastName DESC 
GO 
