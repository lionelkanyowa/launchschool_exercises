# q.3 Using the following code, delete the 'milage' key and its associated value from `car`

car = {
    'type': 'sedan',
    'color': 'blue',
    'milage': 80_000,
    'year': 2003,
}

car.pop('milage')

print(car)