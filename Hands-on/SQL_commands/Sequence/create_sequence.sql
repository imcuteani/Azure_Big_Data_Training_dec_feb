-- Sequence in SQL Server -- 

-- A sequence is a user-defined schema bound object which generates a numeric value
-- according to the specification with which the sequence was created. 

-- The sequence of numeric values are generated in an ascending or descending order
-- at the defined interval 

-- syntax 
-- CREATE SEQUENCE [schema_name] sequence_name
--[AS ] [integer_type]..
--[START_WITH]..
--[INCREMENT BY <constant>] 
-- [MIN_VALUE <constant>]..
--[MAX_VALUE <constant>].. 

use cgsqltraining
GO 

-- Create Schema

create schema Test  
GO 

-- Create Sequence with Increment value of 1 
CREATE SEQUENCE Test.CountBy1
START WITH 1 
INCREMENT BY 1;
GO 

-- Create Sequence with decreased value of 1 

CREATE SEQUENCE Test.CountByNeg1
START WITH 1 
INCREMENT BY -1;
GO 