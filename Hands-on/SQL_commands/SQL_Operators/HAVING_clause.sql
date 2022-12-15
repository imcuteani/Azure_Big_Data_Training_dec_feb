-- Having Clause example -- 

-- HAVING clause in SQL Server is often used to GROUP BY clause to filter 
-- groups based on specified list of conditions. 

-- The GROUP BY clause summarizes the rows into groups and the HAVING clause 
--applies one or more conditions to these groups. 
-- Only the groups which can make the conditions evaluate to TRUE are included in the result. 
-- SQL Server processes the HAVING clause after the GROUP BY clause, 

use "AdventureWorksLT2019"
GO 

SELECT SalesOrderID, SUM(LineTotal) AS SubTotal 
FROM 
SalesLT.SalesOrderDetail
GROUP BY SalesOrderID 
HAVING SUM(LineTotal) > 10000.00
ORDER BY SalesOrderID
GO 