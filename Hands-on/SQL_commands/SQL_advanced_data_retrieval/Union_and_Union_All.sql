-- SQL Server Union operator -- 

-- Combines the result set from two or multiple tables together while 
-- eliminating any duplicates

-- Both of the select statement must have the same number of columns 
-- columns in both the select statement must have compatible data types
-- we can define Group By and Having clause with each select statement. It's not possible
-- to use them with the result set. 
-- we cannot use Order By clause with individual select statement. We can use it 
-- with result set generated from the Union of both select statements. 

-- syntax of Union operator  
select col1, col2, col3 .... coln from tableA 
UNION
select col1, col2, col3 ... coln from tableB;  

use AdventureWorks2016;

-- joining both Person and Employee table based on specific BusinessEntityID and apply UNION operator


select p.LastName, 
p.FirstName
FROM Person.Person p 
JOIN HumanResources.Employee e  
ON p.BusinessEntityID = e.BusinessEntityID
WHERE e.BusinessEntityID = 2 
UNION
select p.LastName, p.FirstName 
FROM Person.Person p JOIN HumanResources.Employee e 
ON p.BusinessEntityID = e.BusinessEntityID
WHERE e.BusinessEntityID = 2
UNION 
select p.LastName,
p.FirstName
FROM Person.Person p JOIN HumanResources.Employee e 
ON p.BusinessEntityID = e.BusinessEntityID
WHERE e.BusinessEntityID = 2


-- UNION All operator will combine the result sets together while preserving any duplicate values


select p.LastName, 
p.FirstName
FROM Person.Person p 
JOIN HumanResources.Employee e  
ON p.BusinessEntityID = e.BusinessEntityID
WHERE e.BusinessEntityID = 2 
UNION ALL
select p.LastName, p.FirstName 
FROM Person.Person p JOIN HumanResources.Employee e 
ON p.BusinessEntityID = e.BusinessEntityID
WHERE e.BusinessEntityID = 2
UNION ALL
select p.LastName,
p.FirstName
FROM Person.Person p JOIN HumanResources.Employee e 
ON p.BusinessEntityID = e.BusinessEntityID
WHERE e.BusinessEntityID = 2





