# Array im PowerShell is a fixed size sequential collectio of elements of the array type 

$mylist = 5.6, 3.4, 6.5, 7.8, 34.0, 23.0, 44.5, 99.45, 110.12
Write-Host("Get the length of the array")
#$mylist.Length


# processing arrays 
Write-Host("Get the fifth index position element of the array")
$mylist[5]

Write-Host("Return partial array")
$sublist = $mylist[1..3]
Write-Host("Lets print the sub list of this array")
$sublist

# add new elements in the first index position of this array 

Write-Host("Assign new values to the array")
$mylist[1] = 100
$mylist

$mylist[6] = 400
$mylist

$mylist[8] = 10.44
$mylist

# removing an element from a specific index position of an array

[System.Collections.ArrayList]$myList = "item1", "item2", "item3", "item4", "item5"
$myList.RemoveAt(2)
$myList

# removing an element from a specific index position of an array 
[System.Collections.ArrayList]$mylist = 5.6, 3.4, 6.5, 7.8, 34.0, 23.0, 44.5, 99.45, 110.12
$mylist.RemoveAt(6)
$mylist

# Remove() removes the first occurance of a specific object from the System.Collections.ArrayList
# RemoveAt() removes element at the specific index of the System.Collections.ArrayList 

#$mylist.Add()

#$mylist.Remove("item1")
#$mylist.IsFixedSize

# Remove the objects from Array list by index position 
#$index = $myList.IndexOf("item2")
#$myList.RemoveAt($index)

# Length property to get the count of the length of the array

$array = "item1", "item2", "item3"
$array.GetType()

# Length property
$array.Length
$array.Count
