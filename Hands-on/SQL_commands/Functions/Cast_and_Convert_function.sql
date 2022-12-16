-- CAST and CONVERT Function in SQL Server 

-- use cast() to convert an expression from one datatype to another data type

-- use cast() function to convert a decimal to another different length 

select CAST(5.90 as DEC(3,0)) result;

-- use cast() function to convert a string to datetime data type 

select CAST('2022-12-16' as datetime) result;

select CAST(5.95 as int) result;

use cgsqltraining;

-- the CONVERT() function converts an expression from one datatype to another datatype. 

-- if the conversion fails, the function will return an error. Otherwise it'll return the converted value. 

select CONVERT(varchar(30), AddressID),
AddressLine1,
AddressLine2,
City,
StateProvince
from Customers.CustomerAddress

-- Benefits of CAST and CONVERT Function in SQL Server 

-- 1. CAST function is used to convert a data type without a specific format
-- 2. CONVERT function is used to do the converting and formatting of the data type at the same time 

-- ISNULL() and Coalesce() function
-- The SQL Coalesce and ISNULL() functions are used to handle NULL values. During the expression
-- evaluation, processes the NULL values & they are replaced with user-defined value. 

-- The SQL Coalesce() function evaluates the argements in order and always return the first non-null value from 
-- the defined argument list 

-- properties of Coalesce() function 

-- 1. Expressions must be same data-type
-- 2. It can contain multiple expressions
-- 3. The SQL coalease function is a syntatic shortcut for case expression

SELECT COALESCE (NULL, NULL, NULL, NULL, 'SQL')

use AdventureWorks2016;

SELECT FirstName + ' ' + COALESCE(MiddleName,' ') + ' ' + LastName FROM Person.Person;   




