# conditional operators in PS 

# $Host - display the name of the current hosting app
# Write-Host - display the output to the terminal of the current hosting app 
# $Error - An array of error objects which display the most recent errors
#$Profile - stores the entire path of a user profile for the defaults shell 
# $NULL - contains empty or null value  

# IF statements in PS 

$x = 10 
if($x -le 20){
    Write-Host("This is IF statement example")
}

# IF-Else statement 

$x = 30 

if($x -le 20){
    Write-Host("This is an IF statement")
} else{
    Write-Host("This is an Else statement")
}

# else-if statement 

$x = 50 
if($x -eq 10){
    Write-Host("Value of X is 10")
} elseif ($x -eq 20){
  Write-Host("Value of X is 20")
} elseif ($x -eq 30) {
    Write-Host("Value of X is 30")
}else {
    Write-Host("This is the Else statement")
}
