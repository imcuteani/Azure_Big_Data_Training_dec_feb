# Operators in PowerShell 

# In PowerShell scripting, there're following operators are available 
# 1. Arithemetic operator 
# 2. Assignment operator 
# 3. Comparison operator
# 4. Logical operator
# 5. Redirectional operator
# 6. Split and join operator
# 7. Type operator 
# 8. Unary operator 

# Arithemetic operators in PS 

$a = 10 
$b = 20
$c = 25
$d = 30 

# addition 

$a + $b 

# substraction 
$a - $b 

# multiplication 

$a * $b 

# division 

$b / $a 

# Modulus 

$b % $a 

# Comparison Operators 

# equal or not

$a -eq $b

# less than

$a -lt $b 

# not equal 

$a -ne $b 

# less than equals

$a -le $b 

# greater than equals

$a  -ge $b 

# Logical Operators 

# AND operators - if both of the variables are non-zero, then the condition becomes true 

$a -AND $b 

# OR operators - if one of the variable values are non-zero, then the condition becomes true

$a -OR $b 


# NOT operator - use to reverse the logical state of its operand. If a condition is true then logical NOT operator will make false

-NOT ($a -AND $b)

# Like operators in PS 

$str1 = "contoso"
$str2 = "fabrikum"

# check the character strings at the end 
$str1 -like '*kum'
$str2 -like '*kum'

# check the character strings at the begining
$str2 -like 'fab*'

# not like operator

$str2 -notlike '*kum*'
$str1 -notlike '*kum*'

# match operators in PS 

$str1 -match '[m$]'

$str1 -notmatch '[k$]'

# redirectional operator in PS 

# redirectional operator assigns the output to be printed into redirected file / output device 
echo "this is PowerShell training" > test.txt
# $cmd > getfile.txt
echo "this is an example of redirectional operator"> newfile.txt

