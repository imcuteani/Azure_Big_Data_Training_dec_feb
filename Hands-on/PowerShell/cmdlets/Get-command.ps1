# Get the details of PowerShell alias, Functions, modules 
Get-Command 

# Display help information about the command Formatted table
Get-Help Format-Table


# Get All services running in your local Windows env 

Get-Service "sql*"

# Get-Members of the SQL processes running in the system
# "|" is called pipe operator in PowerShell scripting which's used to concatenate two commands


Get-Service "sql*" | Get-Member
