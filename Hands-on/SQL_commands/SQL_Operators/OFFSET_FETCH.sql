-- OFFSET FETCH -- 

-- The OFFSET FETCH clauses are the options of the ORDER BY clause. It allows to limit the number of rows to be returned 
-- by the query. 

-- The OFFSET and FETCH clauses are the options of the ORDER BY clause. 

-- Features
-- The OFFSET clause specifies the number of rows to skip before starting to return the rows from the query. 
-- the offset_row_count can be a constant, variable, or parameter which is greater or equal to zero. 

-- The FETCH clause specifies the number of rows to return after the OFFSET clause has been processed. The offset_row_count
-- can be constant, variable or scaler which is greater or equal to one. 

-- The OFFSET clause is mandatory while the FETCH clause is optional, also , the first and the next are synonms respectively so you can use them interchangably. 

-- OFFSET clause helps to identify how many number of rows / records to skip fron the query. 
-- the FETCH clause specifies the number of rows to return after the OFFSET clause has been processed. 

-- limit the number of rows returned by a query 

-- OFFSET row_count {ROW | ROWS}

-- Skip the first 10 rows and return the rest of rows 

use AdventureWorksLT2019;

select Name, 
ListPrice
FROM 
SalesLT.Product
ORDER BY 
ListPrice, 
Name 
OFFSET 10 ROWS; 

select * from SalesLT.Product

-- Skip the first 20 rows and select the next 30 rows/ products, use both OFFSET and FETCH clause. 

select 
Name, 
ListPrice
FROM
SalesLT.Product
ORDER BY
ListPrice ASC
OFFSET 20 ROWS
FETCH NEXT 30 ROWS ONLY; 

