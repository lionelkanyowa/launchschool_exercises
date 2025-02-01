# q.6 Write a function that checks whether a string is empty or not:

def string_is_empty(string):
    if string == '':
        return True
    else:
        return False

print(string_is_empty('mars'))
print(string_is_empty(''))
print(string_is_empty(' '))