-- Limitation of ROW_Number() function 

-- The Row_Number() function does not always return the same results if there're duplicates
-- values within the ORDER BY clause which is specified. 
-- The column which is defined with the ORDER BY clause if having duplicate values
-- then the row_number() function does not return the expected sequential records in the resultset. 

-- RANK function is sequential ordering of rows 
-- duplicate values will receive the same rank value 
-- will produce gaps in the sequence of returned rows when ties exist
-- leave the gaps in the bunch of sequence of row groups 



-- Difference between Row_NUMBER() and RANK() function, 

-- 1. RANK(), DENSE_RANK() are similar to ROW_NUMBER function, but when there are ties, they will give the same to the value to the tied values. 
-- rank() function will the ranking. so the numbering will go 1, 2, 2, 4 based on ranks. 

-- RANK() OVER(
    --[PARTITION BY expression,]
    --ORDER BY expression (ASC | DESC); 

    -- The RANK() function is in SQL Server is used to calculate a rank for each row within a partition of a result set 


use AdventureWorks2016; 

select 
RANK() OVER(ORDER BY FirstName) rank_value,
    FirstName, 
    LastName, 
    ModifiedDate
    FROM Person.Person;

    -- DENSE_RANK() function will not leave any gaps between the rank groups 

    select 
DENSE_RANK() OVER(ORDER BY FirstName) dense_rank_value,
    FirstName, 
    LastName, 
    ModifiedDate
    FROM Person.Person;

-- difference between RANK() and DENSE_RANK() function 

    -- RANK() function will assign randomized ranking values for distinct and duplicate set of records 
    -- DENSE_RANK() function will assign specific sequential sorted ranking order for distinct and duplicate set of rank groups. 