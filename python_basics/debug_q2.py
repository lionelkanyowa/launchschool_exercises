# q.2 Our predict_weather function should output a message indicating whether a sunny or cloudy day lies ahead. 
# However, the output is the same every time the function is invoked. Why? Fix the code so that it behaves as expected.

import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()

# Problem: The booleans in line 7 were string types, hence when the function is called, it will default to outputting 
# the `True` statement "Today's weather will be sunny!" 
# 
# By removing the quotation marks between the True, False string we now have booleans that will return a truthy or falsy
# value at random.
