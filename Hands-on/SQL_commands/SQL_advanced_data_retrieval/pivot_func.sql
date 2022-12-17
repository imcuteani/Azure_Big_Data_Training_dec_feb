-- Pivot Function in SQL Server -- 

-- Pivot functions are associated with the Pivot tables

-- Pivot tables are used to show the summarized or calculated results which are
-- generated from a large dataset. 
-- it's used to report on the specific dimensions from the vast dataset where 
-- users can convert rows into the columns 

-- Pivot tables are calculated by using the Pivot Operator

-- Benefits of Pivot function 

-- gives up the table - valued expressions. 
-- turns the unique values in one column into multiple columns and it 
-- performs the aggregation on remaining values 

use AdventureWorks2016; 

-- retrieve the yearwise sales purchase values 

select VendorID, [2001], [2002], [2003], [2004]
FROM (SELECT VendorID, PurchaseOrderID, Year(OrderDate)SubTotal
FROM Purchasing.PurchaseOrderHeader) r   
PIVOT(COUNT(r.PurchaseOrderID)
FOR SubTotal
IN ([2001], [2002],[2003], [2004]))
AS Results
ORDER BY VendorID;
