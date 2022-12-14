-- self join in SQL Server -- 

-- A self join is mechanism of joining the table itself. You would use a self join 
-- when you wanted to create a result set joining records in the table with some other records 
-- from the same table

-- A self join uses inner join or left outer join. 
-- query which uses the self join refers to the same table, the table is used to assign different names 
-- to the same table within the query 

use AdventureWorks2016;

select m.ManagerID as 'ManagerID',
M1.ContactID AS 'ManagerContactID',
M1.FirstName AS 'ManagerFirstName',
M1.LastName AS 'ManagerLastName',
M.Title AS 'ManagerTitle',
E.EmployeeID AS 'EmployeeID',
E1.ContactID AS 'EmployeeContactID',
E1.FirstName AS 'EmployeeFirstName',
E1.LastName AS 'EmployeeLastName',
E.Title AS 'EmployeeTitle'
FROM HumanResources.Employee E 
INNER JOIN HumanResources.Employee M 
ON E.ManagerID = M.EmployeeID 
INNER JOIN Person.Contact E1 
ON E1.ContactID = E.ContactID 
INNER JOIN Person.Contact M1
ON M1.ContactID = M.ContactID 
ORDER BY M1.LastName


select c.ContactID, 
c.Name,
sp.SalesPersonID,
sp.SalesYTD,
sp.SalesLastYear,
sp.Bonus,
st.TerritoryID,
st.Name,
st.[group],
st.SalesYTD
FROM 
Person.ContactType c 
INNER JOIN Sales.SalesPerson sp 
ON c.ContactID = sp.ContactID 
LEFT OUTER JOIN Sales.SalesTerritory st 
ON st.TerritoryID = sp.TerritoryID
ORDER BY st.TerritoryID, c.Name


use AdventureWorksLT2019;

select a.ProductID, a.Name, b.SalesOrderID 
FROM SalesLT.Product as a 
INNER JOIN 
SalesLT.SalesOrderDetail as b 
ON a.ProductID = b.ProductID AND a.Color = 'Black'
ORDER BY a.Name;