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

-- DATEDIFF() function 

-- DATEDIFF() function returns the number of date and time difference crossed between specified dates an an int 

select DATEDIFF(DAY, 2019-31-01,2019-01-01) as 'datediff';

-- DATEADD() function 

-- add a new day to any specific date 

select DATEADD(DAY, 1, GETDATE()) as 'DATEPlus';

-- DATEPART() function 

-- returns an integer corresponding to the datepart specified 

select DATEPART(YEAR, GETDATE()) as 'Year';
select DATEPART(DAYOFYEAR, GETDATE()) as 'DayofYear';
select DATEPART(DAY, GETDATE()) as 'Day';
select DATEPART(WEEK, GETDATE()) as 'WeekofYear';
select DATEPART(HOUR, GETDATE()) as 'Hour';
select DATEPART(MINUTE, GETDATE()) as 'Minute';
select DATEPART(SECOND, GETDATE()) as 'Second'; 