# PowerShell Provider 

# A provider allows to access data and components which would not otherwise be easily accessible at the command line. 
# the data is presented in a consistent format which resembles a file system drive.

# List of PowerShell Providers 

#1. Get-PSProvider
#2. Get-FunctionProvider
#3. Get-CertificateProvider
#4. Environment-provider
#5. Variable-provider
#6.certification provider 

# The data could be exposed on drive, and it can accessed via a path like a disk drive 

# Get information about one or more providers 

# Get-PSProvider

# Get provider information 

Get-PSDrive Function | Format-List * 

# Set the location to another drive 

Set-Location D: 