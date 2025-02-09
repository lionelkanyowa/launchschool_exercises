# q.4 When the user inputs 10, we expect the program to print `The result is 50!`, But that's not the output we see.
# Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input()) # added the `int` constructor so that input() returns an `int` type.

print(f"The result is {multiply_by_five(number)}!")

# Problem: The result of the input is returning a string. We need to specify that the input type should be
# a string type in line 8.