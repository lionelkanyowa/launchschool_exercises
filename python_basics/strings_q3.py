# q.3 Using the following code, compare the value of name with the string 'RoGeR' while 
# ignoring the case of both strings. Print true if the values are the same; print false if they aren't. 
# Next, perform a case-insensitive comparison between the value of name and the string 'DAVE'.

name = 'Roger'
other_name = 'RoGeR'

this_name = 'DAVE'
print(name.casefold() == other_name.casefold())
print(name.casefold == this_name.casefold())
