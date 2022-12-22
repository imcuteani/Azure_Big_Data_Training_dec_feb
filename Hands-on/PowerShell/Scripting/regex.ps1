# Regular Expression in PS scripts 

# example of supported regular expressions through Match characters 

"book" -match "mm"

# Logic matches with any of the single character

"copy" -match "m..n"

# Logic matches at one of characters in the brackets 

"big" -match "b[iou]g"

# Matches with at least of one of the characters found within the range or not 

"second" -match "[a-e]nd"

# Match begining of characters 

"book" -match "^bo"

# Match to check the ending of characters 

"book" -match "om$"

