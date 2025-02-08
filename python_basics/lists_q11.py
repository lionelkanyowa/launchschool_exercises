# q.11 We have a grocery list. As we check off items on that list, from the top of the list to the bottom, 
# we want to remove from the list. 

# Write code that removes the items from the `grocery_list`, one by one, until it is empty. If you
# print the elements you remove, the expected behavior would look as follows:

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

for item in range(len(grocery_list)):
    print(grocery_list.pop())
    

print(grocery_list)

# Expected output:
# paprika
# tofu
# garlic
# quinoa
# carrots
# broccoli
# hummus
# []
