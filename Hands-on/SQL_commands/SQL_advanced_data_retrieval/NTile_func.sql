-- NTile() function in SQL Server 

-- NTILE() function is used to split a result set into N number of buckets of equal sizes 

-- NTILE() function is a window function() that distributes rows of an ordered partition into a pre-defined number of 
-- roughly equal groups. It assigns each group a number_expression ranging from 1. 
-- The NTILE() function assigns a number_expression for every row in a group where each row belongs. 

-- Syntax for NTILE() func

--NTILE(number_expression) OVER(
--    PARTITION BY partition_expression ] 
 --   ORDER BY sort_expression [ASC | DESC]

--)

-- number_expression - the number_expression is the integer into which the rows are divided. 
-- PARTITION_BY clause - is optional, it differs the rows of a result set into partitions where the NTILE() function is used. 
-- ORDER BY clause - The ORDER BY clause defines the order of rows in each partition where the NTILE() is used. 

use AdventureWorks2016;

select ProductID, 
ProductNumber,
NTILE (4) OVER (
    ORDER BY ProductNumber
) ntile_group 
FROM Production.Product

select ProductID, 
NTILE (4) OVER (
    ORDER BY ProductID
) ntile_group_productID 
FROM Production.Product
