# q.1 You came across the following code. What does it raise for the given examples and what exactly do the error 
# messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0) 
find_first_nonzero_among(1)

# It raises a `TypeError` because our function in line 1 only accepts 1 positional argument. However we see that
# in line 9, 6 positional arguments were given. 

# Another `TypeError` is raised for the function call in line 10. Although it receives the correct number of arguments, 
# In line 5 when we try to iterate n in numbers, an error is raised because `int` objects are not iterable
