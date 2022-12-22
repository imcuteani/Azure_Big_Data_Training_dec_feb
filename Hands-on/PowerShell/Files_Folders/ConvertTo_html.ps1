# ConvertTo-HTML 

# The ConvertTo-HTML cmdlet converts a .NET object into HTML which can be displayed in a web browser

# you can use this cmdlet to display the output of a command in a web page

# you can use the parameters of ConvertTo-Html to select object properties. 
# to specify a table or list format. to specify this Html page title, to add text 

# create a web page in html to get current date in PS 

ConvertTo-Html -InputObject (Get-Date) | Out-File get-date.html
Invoke-Item get-date.html

# Get the alias details through PowerShell command & convert it into Html 

Get-Alias | ConvertTo-Html | Out-File aliases.html 
Invoke-Item aliases.html