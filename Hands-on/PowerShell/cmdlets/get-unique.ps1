# Cmdlets 

# A cmdlets or command list is a lightweight command used in the Windows PowerShell environment. 
# the windows powershell runtime invokes these cmdlets at command prompt

# you can create and invoke them programmatically through the Windows Powershell API. 

# Cmdlet 

# Type of the following command in the PS console 

$list = "one", "two", "two","three", "four", "five", "five", "six"

# Get the print of the original list of strings

$list 

# we're sorting the list and get the unique values. 

$list | sort | Get-Unique