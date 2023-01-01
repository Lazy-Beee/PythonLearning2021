number = int(input('Enter an integer: '))
if number % 2 == 0:
    print(f'The integer {number} is even.')
else:
    print(f'The integer {number} is odd.')

fruit = ['a', 'b', 'a', 'c', 'a']
new_fruit = []
while fruit:
    new_fruit.append(fruit.pop())
print(new_fruit)

while 'a' in new_fruit:
    new_fruit.remove('a')
print(new_fruit)
