# q.10 Write a function that counts the number of occurrences of a substring in a string.

def count_substrings(string, substring):
    return string.count(substring)

print(count_substrings("lemon lemon lemon", "lemon"))
print(count_substrings("laLAlaLA", "la"))
print(count_substrings("launch", "uno"))