# You want to have a small script delivering motivational quotes, but with the following code you run into a 
# very common error message: TypeError: can only concatenate str (not "NoneType") to str. What is the 
# problem and how can you fix it?

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mines are still greater.'

print('Confucius says:')
print('"'+ get_quote('Confucius') + '"')

# Problem: Each of the if block within the function was returning a `None` because we did not specify for the strings 
# to be explicitly returned. By using the `return` keyword on the strings within each of the if blocks, we should now
# see the string being returned when we call the function in line 14.    