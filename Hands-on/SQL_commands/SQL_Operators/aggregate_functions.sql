-- Aggregate Functions -- 

-- Aggregate Function is used to perform the calculation on one or more 
-- values and returns a single value. The aggregate function often is used 
-- with the GROUP BY , HAVING clause for the select statement

-- AVG - calculate the average of the non-null values in a dataset

-- COUNT - returns the no of rows in a group, including the rows with the NULL value 

-- MIN - returns the minimum value (lowest) in a set of non-null values 

-- MAX -- returns the maximum value (highest) in a set of non-null values

-- SUM -- summation of all non-null values in a set

-- STDDEV -- returns the standard deviation of all values provided for the expression, but does so based on sample of the data population

-- STDEVP -- returns the standard deviation of all values provided for the expression, based on the entire data population

-- VAR -- Statistical variance of values in expression based on specified data samples

-- VARP -- statiscal variance of values in expression based on entire data population set 

-- DISTINCT -- return only the distinct values in the result set 

-- COUNT_BIG -- function returns the number of rows (with BIGINT data type) in a group, including rows with the NULL values. 

-- CHECKSUM_AGG -- function that calculates the checksum value based on group of rows. 

-- AVG() example 

use "AdventureWorksLT2019"
GO 

select AVG(UnitPrice) avg_order_price 
FROM 
SalesLT.SalesOrderDetail


