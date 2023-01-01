alph = ['a', 'b', 'c', 'd']
print(alph)
alph.append('e')
print(alph)
alph.pop()
print(alph)
alph.remove('b')
print(alph)
alph.insert(1, 'b')
print(alph)

print('--------------------')
alph.reverse()
print(alph)
print(sorted(alph))
alph.sort()
print(alph)
print(alph[len(alph)-1])
print(alph[-1])

print('--------------------')
numbers = list(range(0, 13, 3))
print(numbers)
squares = [value ** 2 for value in numbers]
print(squares)
print(numbers[1:4])
print(numbers[3:])
numbers2 = numbers[:]
print(numbers2)

