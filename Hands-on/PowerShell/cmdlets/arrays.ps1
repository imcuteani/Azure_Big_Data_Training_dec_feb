# Array im PowerShell is a fixed size sequential collectio of elements of the array type 

$mylist = 5.6, 3.4, 6.5, 7.8, 34.0, 23.0, 44.5, 99.45, 110.12
Write-Host("Get the length of the array")
$mylist.Length


# processing arrays 
Write-Host("Get the fifth element of the array")
$mylist[5]

Write-Host("Return partial array")
$sublist = $mylist[1..3]
Write-Host("Lets print the sub list of this array")
$sublist

# add new elements in the array 

Write-Host("Assign new values to the array")
$mylist[1] = 100
$mylist
