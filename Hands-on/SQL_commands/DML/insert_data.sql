use "cgsqltraining"
go 

SET IDENTITY_INSERT [Customers].[CustomerAddress] ON
INSERT INTO Customers.CustomerAddress
(AddressId,
AddressType,
AddressLine1,
AddressLine2,
AddressLine3,
City,
StateProvince,
Country)
VALUES 
(1,
'local'
 ,'seattle'
 ,''
 ,''
 ,'Seattle',
 '',
 'united states')
GO