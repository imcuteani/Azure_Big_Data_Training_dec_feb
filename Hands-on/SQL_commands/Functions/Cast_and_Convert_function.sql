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