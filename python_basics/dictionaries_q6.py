# q.6 Check whether the keys `name` and `grade` exist in the following dictionary:

student = {
    'id': 123,
    'grade': 'B'
}

print(student.get('name', "Not found"))
print(student.get('grade', "Not found"))

