-- ROW_Number() in SQL Server 

-- ROW_NUMBER() actually helps to provide the numbers in a result set sequentially 
-- from 1 to n based on the user-specified ordering 
-- break the result set into GROUPS and NUMBERS based on the rows to be displayed within 
-- the group by applying a PARTITION BY clause 

-- PARTITON BY () clause divide the result set into partitions (another term for group of rows)
-- The Row_Number() function is applied to each partition seperately and reinitialized the row number for each partition

-- Partition BY() clause is option, if skipped, then ROW_NUMBER() function will treat the whole result set as a single partition

-- ORDER BY() clause defines the logical order of the rows within each partition of the result set. The
-- ORDER BY clause is mandatory because the ROW_NUMBER() function is order sensitive. 

-- OVER() is a method which determines the partitioning and ordering of a rowset before the ROW_NUMBER() function is applied 
use AdventureWorks2016; 

select 
ROW_NUMBER() OVER(ORDER BY FirstName) row_num,
    FirstName, 
    LastName, 
    ModifiedDate
    FROM Person.Person;

-- Partition BY() clause along with ORDER BY clause applied with ROW_NUMBER() function


-- We used the PARTITION BY clause to divide the Persons into partitions by ModifiedDate. 
-- The Row_Number was reinitialized when the modified_date has changed. 

    select FirstName, 
    LastName,
    ModifiedDate,
    ROW_NUMBER() OVER (
        PARTITION BY ModifiedDate
        ORDER BY FirstName
    ) row_num 
    FROM Person.Person
    ORDER BY ModifiedDate;

     select FirstName, 
    LastName,
    PersonType,
    ModifiedDate,
    ROW_NUMBER() OVER (
        PARTITION BY PersonType
        ORDER BY FirstName
    ) row_num 
    FROM Person.Person
    ORDER BY PersonType;


