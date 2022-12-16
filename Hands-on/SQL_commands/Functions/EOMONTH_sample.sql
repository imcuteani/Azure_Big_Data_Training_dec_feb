-- SQL Server EMONTH function -- 

-- built-in SQL Server function provides the last day of the month based on specified input date 

use cgsqltraining;

select EOMONTH('2022-10-01') end_of_month_dec22;

-- passing a date with a month represents leap year 

select EOMONTH('2020-02-15') end_of_month2020;

-- to get the total number of days in a specified month 

select DAY(EOMONTH('2022-12-16')) DAYS;

