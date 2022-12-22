# For loop in PowerShell

# array in powershell is a fixed size sequential collection of elements of array type. 
# An array is used to store a collection of data with various data type
# An array is often though is like a collection of objects 

$mylist = 5.6, 3.4, 6.7, 8.5, 10.2, 11, 23, 32.4, 45.4 
Write-Host("Print the array elements")
$mylist

# For loop executes a sequence of statements multiple times and manages the loop variable

$array = @("item1", "item2", "item3")

for($i = 0; $i -lt $array.Count; $i++) {
    $array[$i]
}


# Foreach loop 

# enhanced for loop. It's used to traverse collection of elements including arrays

# access over the elements of a loop based on each specific variable value 

$array = @("number1", "number2", "number3")
foreach($element in $array) {$element}

# another example to show foreach loop 

$array | foreach {$_}

# While loop 

$array = @("item1", "item2", "item3")
$counter = 0;

while($counter -lt $array.length) {
 $array[$counter]
 $counter = $counter + 1
}