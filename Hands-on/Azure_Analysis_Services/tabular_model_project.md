	Hands-on Lab 02 
	
	Tabular Model Development & Deployment to AAS/SSAS Services 
	
	Goals- 
	
	1. Create a new tabular model project 
	2. How to import data from SQL Server db/ Azure SQL DW db into the tabular model project
	3. Mark the DimDate table as date table
	4. Rename the column of specific table (dimDate) table. 
	5. Set the Mark as Date table
	6. Create and manage relationships between the tables in the model (PK/FK constraints) 
	7. Create and manage the calculated columns using DAX , measures
	8. KPIs (Knowledge performance Indicators) for analysis
	9. Create the hierarchies 
	10. Create the partitions dividing the table data into the smaller logical parts. 
	11. Apply security model objects
	12. Deploy the tabular model in AAS. 


Pre-requisites of the lab 

	1. Visual Studio 2017/2019 
	2. Compatible SQL Server DB engine (2017/2019) 
	3. SSMS
	4. AdventureWorksDW edition 
	5. Azure SQL Data warehouse instance with sample AdventureWorks DW db 
	6. PBI desktop
	7. An Azure Analysis Service instance (Azure subscription) , SSAS 


Tasks for today as pre-requisites for hands-on lab 02

	1. Provision the Azure VM (with the same SKU as previous) 
	2. Provision the Azure SQL DW with sample adventureworks db 
	3. Login into the Azure VM & then install Visual Studio 
	4. Create the tabular model project with analysis service extension 

https://developerinsider.co/download-visual-studio-2019-web-installer-iso-community-professional-enterprise/#downloadvisualstudio2019iso



Links: 

https://developerinsider.co/download-visual-studio-2019-web-installer-iso-community-professional-enterprise/#downloadvisualstudio2019iso

https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16

https://download.microsoft.com/download/4/8/6/486005eb-7aa8-4128-aac0-6569782b37b0/SQL2019-SSEI-Eval.exe

	
	
	 Steps for this lab
	
	1. Provision an Azure VM (sufficient memory required) 
	2. Provision SQL Server 2017 with SSDT 
	3. Install SSMS and PBI desktop 
	4. Download the AdventureWorks DW db 
	5. Visual Studio community edition 2017/2019. 
	
	
	
	DimCustomer, DimDate, DimGeography, DimProduct, DimProductCategory, DimProductSubCategory, FactInternetSales
	
	
	
	DimCustomer - Remove Columns - SpanishEducation, FrenchEducation, SpanishOccupation, FrenchEducation
	DimDate -  Remove Columns - SpanishDayNameOfWeek, FrenchDayNameOfWeek, SpanishMonthName, FrenchMonthName
	DimGeoGraphy - Remove Columns - SpanishCountryRegionName, FrenchCountryRegionName
	DimProduct - Remove Columns - SpanishProductName, FrenchProductName, FrenchDescription, ChineseDescription, ArabicDescription, HebrewDescription, ThaiDescription, GermanDescription, JapaneseDescription, TurkishDescription
	DimProductCategory - SpanishProductCategoryName, FrenchProductCategoryName
	DimProductSubCategory - SpanishProductSubCategoryName, FrenchProductSubCategoryName
	FactInternetSales - no need to remove any columns 


    Calculated columns created through DAX formula

    Calculated Column 

1. MonthCalendar - =RIGHT(" " & FORMAT([MonthNumberOfYear],"#0"), 2) & " - " & [EnglishMonthName]

2. DayOfWeek = =RIGHT(" " & FORMAT([DayNumberOfWeek],"#0"), 2) &  " - "  &[EnglishDayNameOfWeek]

3. Rename the column as ProductCategoryName of DimProduct table =RELATED('DimProductSubcategory'[EnglishProductSubcategoryName])

4. Bring the column EnglishProductCategoryName from DimProductCategory table = =RELATED('DimProductCategory'[EnglishProductCategoryName])

5. Calculate the product margin from the FactInternetSales table   =[SalesAmount]-[TotalProductCost]
	
