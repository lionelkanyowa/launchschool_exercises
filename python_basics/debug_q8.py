# We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game. However, we encountered an issue, as
# whenever we change a value in one nested list, all nested lists are affected. can you fix the code?

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(list(sub_list))



matrix[0][0] = "X"
print(matrix)   # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

# list.append() does not create a new value, but rather returns the original value and this means that when we use the 
# append() method, we are return the original nested list 3 times, so any changes made in the first list will affect other
# lists. To resolve this, we can use  list.copy, list(sublist) or [:]