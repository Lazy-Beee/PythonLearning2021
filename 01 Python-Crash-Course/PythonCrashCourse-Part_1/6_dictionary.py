fruit = {'name': 'apple', 'color': 'red'}
print(fruit)

fruit['taste'] = 'sweet'
fruit['size'] = 'medium'
print(fruit)
fruit['color'] = 'green'
print(fruit['color'])

del fruit['color']
print(fruit)
print(fruit.get('name', 'No name assigned'))
print(fruit.get('color', 'No color assigned'))

print('-------------------')
for key, value in fruit.items():
    print(f'Key: {key}  Value: {value}')

print('-------------------')
for key in fruit.keys():
    print(f'Key: {key}')

values = set(fruit.values())
print(values)