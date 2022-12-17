-- Choose Function 

-- it's available in tSQL to return the item at the specified index from the list of values 

-- an item can also be retrieved as the specific index position from the list 

-- CHOOSE(index, value[1], value[2]... value[n])

-- return of items depends on the index 
-- depends on the items, helps to pick the item as per the index specified


use AdventureWorks2016;

-- retrieve the distinct names of the person, date and specific month in SQL query through CHOOSE function

select 
DISTINCT(FirstName + ' '+ LastName) AS NAME 
, DATEPART(DD, ModifiedDate) AS [Date]
, CHOOSE(DATEPART(MM, ModifiedDate), 'January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December')[Month]
, DATEPART(YYYY, ModifiedDate) AS [YEAR]
FROM Person.Person 
ORDER BY Name ASC 


