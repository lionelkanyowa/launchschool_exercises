# q.10 You've been asked to implement a function called digit_product that takes a string of 
# digits as an argument and returns the product of all the digits in the string.

# When testing the function, you find out that it returns `0`, which is not what you expect. 
# Can you identify the issue and correct the code?

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    # product = 0  changed the product variable to initialize to 1. Starting at 0 means every 
    # digit results to zero including the final answer. 
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result) # expected: 120, actual: 0