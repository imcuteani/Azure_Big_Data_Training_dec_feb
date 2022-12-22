# ConvertTo-Csv cmdlet

# The ConvertTo-Csv cmdlet returns a series of comma seperated value (CSV) strings which represent the objects 
# which we can submit

# we can use ConvertTo-Csv cmdlet to recreate objects from the Csv strings
# that represent the objects which we submit 

# the objects converted from csv are string values of the original objects that contain the property values and no methods

# Convert an object to CSV 

# Convert the process object to a CSV string 

# retrieve the process details filtered to "PowerShell" objects & convert it to csv file 

Get-Process -Name 'PowerShell' | ConvertTo-Csv -NoTypeInformation > process.csv 

# Convert a DateTime object to CSV string

$Date = Get-Date 

ConvertTo-Csv -InputObject $Date -Delimiter ':' -NoTypeInformation > date.csv


