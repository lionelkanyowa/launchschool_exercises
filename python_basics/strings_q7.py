# Write an `is_empty_or_blank` function to determine whether a string is either empty or consists
# entirely of spaces
def is_empty_or_blank(string):
     if string == '':
       return True
     elif string == ' ':
       return True
     else:
       return False

# def is_empty_or_blank(string):
    # return not string or string.isspace()


print(is_empty_or_blank('mars'))
print(is_empty_or_blank(' '))
print(is_empty_or_blank(''))