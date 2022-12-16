-- Cross join in SQL server -- 

-- A cross join returns all rows for all possible combinations of two tables. 
-- It generates all the rows from the left table which is then combined with all the rows from 
-- the right table. 
-- This type of join (cross-join) is also called a Cartesian Product (A*B)

use "AdventureWorks2016";

-- retrive the EmployeeName, BusinessEntityID from Employee table and department from the Department table

select a.BusinessEntityID, b.Name AS Department
FROM 
HumanResources.Employee as a 
CROSS JOIN 
HumanResources.Department as b; 


use cgsqltraining;

select a.CustomerID,
a.CompanyName,
a.FirstName,
a.LastName,
b.FirstName,
b.LastName
FROM 
Customers.Customer a
CROSS JOIN 
HumanResources.Employee b;