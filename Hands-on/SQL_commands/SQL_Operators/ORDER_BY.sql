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

-- using 