# q.10 What will the following code do and why? Don't run until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# Line 9 will output '[1, 2, 3], this is because it is referencing to the global variable in line
# 3. Given that we are trying to reassign the global variable in line 6 this means 
# these are 2 different variables. 

# Correct answer:
# Line 9 will output '[10, 2, 3]'. within the function in line 6, b is not a local variable, but rather 
# it is referencing the b in the global scope on line 3. And since lists are mutable, this means that 
# the global variable b can be mutated within the function.
