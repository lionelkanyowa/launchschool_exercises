# q.9 Write a function that checks whether a string starts with a specif prefix.

def starts_with(str1, str2):
    return str1.startswith(str2)

print(starts_with("launch", "la"))
print(starts_with("school", "sah"))
print(starts_with("school", "sch"))