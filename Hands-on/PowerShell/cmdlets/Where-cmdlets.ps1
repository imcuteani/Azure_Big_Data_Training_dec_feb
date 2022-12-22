#Where-object cmdlet can be used to select the objects having a particular property values from the collection of 
# objects which're passed to it

# Get the list of all stopped and running services 

Get-Service | Where-Object {$_.Status -eq "Stopped"}

Get-Service | Where-Object {$_.Status -eq "Running"}

# Get Processes based on a process name 

#Get the list of Windows processes that matches with the alphabet of p 

Get-Process | Where-Object {$_.ProcessName -match "^p.*"}