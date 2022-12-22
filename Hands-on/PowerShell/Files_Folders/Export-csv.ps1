# Export-Csv 

# This cmdlet creates a CSV file of the objects which you submit
# each object is a row includes the comma separated list of objects property values
# we can use the Export-Csv cmdlet to create spreadsheets

# List out the process details and export the output in the csv format & read the content

Get-Process | Export-Csv -Path .\Process.csv -NoTypeInformation 
Get-Content -Path .\Process.csv 