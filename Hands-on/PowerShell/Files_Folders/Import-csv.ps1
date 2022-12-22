#Import-Csv 

# read the contents of the csv file and import the objects from the CSV file 

# Get-Process cmdlet sends process objects down the pipeline to the Export-Csv. 
# The Export-Csv cmdlet converts the process objects to CSV strings and save the strings in the process.csv file

$P = Import-Csv -Path .\Process.csv

$P | Format-Table