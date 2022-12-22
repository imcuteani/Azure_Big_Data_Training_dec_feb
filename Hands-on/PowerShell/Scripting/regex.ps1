# Regular Expression in PS scripts 

# example of supported regular expressions through Match characters 

"book" -match "mm"

# Logic matches with any of the single character

"copy" -match "a..b"

"book" -match "a..c"

# Logic matches at one of characters in the brackets 

"big" -match "b[iou]g"

# Matches with at least of one of the characters found within the range in the begining of alphasets/charaters and the next set of characters  or not 

"second" -match "[a-e]nd"

"second" -match "[r-t]ec"

"and" -match "[a-e]nd"

# Match begining of characters 

"book" -match "^bo"

# Match to check the ending of characters 

"book" -match "om$"

