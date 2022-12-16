-- FULL OUTER JOIN -- 

-- Based on the two tables specified in the join clause
-- all data is retrieved from both of the two tables regardless of matching data

-- preserves the contents of both of the left-side and right-side tables. 
-- when a match does not exist, a NULL will appear in the result. 

use AdventureWorksLT2019;

-- join the Product and SalesOrderDetail table through Full Outer join 
-- based on criteria i.e. ProductID and retrieving all data from both of the
-- two tables regardless of matching data 

select a.ProductID, 
a.Name,
b.SalesOrderID 
FROM SalesLT.Product a 
FULL OUTER JOIN SalesLT.SalesOrderDetail b 
ON a.ProductID = b.ProductID 
ORDER BY 1; 
