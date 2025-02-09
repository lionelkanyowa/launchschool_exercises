# Magdalena has just adopted a new pet! She wants to add her new dog, Bowser, to the pets dictionary. After 
# doing so, she realizes that her dogs Sparky and Fido have been mistakenly removed. Help Magdalena fix her 
# code so that all three of her dogs' names will be associated with the key 'dog' in the pets dictionary.

pets = {'cat': 'pepe', 
        'dog': ['sparky', 'fido'], 
        'fish': 'oscar',
        }

pets['dog'].append('bowser') # Using the append() method to retain the original list while adding in a list string.

print(pets) # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

# Problem: when using key-based index access on line 10, The values associated with the 'dog' key are are within a list
# which would be considered as one value, therefore when adding 'bowser', we are actually removing the whole value.

