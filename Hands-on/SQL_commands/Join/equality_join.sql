--equality join -- 

-- common form of sql inner join. If the inner join contains an equality operator 
-- "=" , then it's called equi/equality join

use AdventureWorks2016

select b.ProductID,
b.Name,
b.ListPrice,
a.UnitPrice AS 'SalesPrice'
FROM 
Sales.SalesOrderDetail as a 
JOIN Production.Product as b 
ON a.ProductID = b.ProductID AND a.UnitPrice < b.ListPrice 
WHERE b.ProductID = 365; 

-- select * from Production.Product;

select p1.BusinessEntityID, p1.ProductID 
FROM 
Purchasing.ProductVendor p1 
INNER JOIN Purchasing.ProductVendor p2 
ON p1.ProductID = p2.ProductID
WHERE p1.BusinessEntityID <> p2.BusinessEntityID
ORDER BY p1.ProductID;

