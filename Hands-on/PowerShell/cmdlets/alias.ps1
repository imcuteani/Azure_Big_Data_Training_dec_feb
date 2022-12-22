# Alias in PowerShell 

# An Alias is an alternate name for a command. A command can have multiple alias. The original name and all of the 
# alias can be used interchangeably. An Alias can be reassigned, an alias is an item which represents a command. 

# An Alias can be assigned to another alias. 
#however, the new alias is not an alias of the original command. 

# the provider of an alias is a flat namespace which contains only objects that represents the alias. 
# the variables have no child items

# create an alias 

New-Alias

New-Alias -Name gh -Value Get-Help

# Change the alias 
Set-Alias -Name gc -Value Get-Command

# Get the information from Alias 

Get-Alias  