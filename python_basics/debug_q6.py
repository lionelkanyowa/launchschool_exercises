# You want to add the numbers from 1 to 5 to a list, but the code below is not producing the expected result.
# How can you fix it?

numbers = []

for i in range(1, 6): # Changed range(5) to range(1, 6). i starts at 1 and stops at 6 with the output being [1, 2, 3, 4, 5]
    numbers.append(i)

print(numbers)