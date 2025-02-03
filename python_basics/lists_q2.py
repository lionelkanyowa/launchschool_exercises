# q.2 Write a function that returns th last element of a list provided as an argument:
def last(lst):
    # return(lst.pop() if lst else "No elements in list") # This alters th list 
    return(lst[-1] if lst else "no elements in the list")

print(last(['Earth', 'Moon', 'Mars']))
print(last([]))
print(last(['Rock', 'Paper', 'Scissors', 'Game', 'Win']))
print(last([3, 4, 5, 6, 10, 2, 4]))

