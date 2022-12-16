-- built - in DATE functions in SQL Server -- 

-- datetime
-- datetime2
-- date
-- time
-- datetimeoffset 

-- sysdatetime() - returns the date and time of the system where the SQL server is running
-- sysdatetimeoffset() - returns the date and time of the system where SQL server is running + UTC offset 
-- sysutcdatetime() - returns the date and time of the system where the SQL Server is running on as UTC timezone

select SYSDATETIME() as 'DateAndTime'; -- return the datetime2
select SYSDATETIMEOFFSET() as 'DateAndTimeOffset' -- return the datetimeoffset
select SYSUTCDATETIME() as 'DateAndTimeUtc' -- returns datetime2

select GETDATE() as 'DateAndTime'; 

-- DateName() function

-- returns a string corresponding to the datepart specified for the given date

select DATENAME(YEAR, GETDATE()) as 'Year';
select DATENAME(QUARTER, GETDATE()) as 'Quarter';
select DATENAME(MONTH, GETDATE()) as 'Month'; 