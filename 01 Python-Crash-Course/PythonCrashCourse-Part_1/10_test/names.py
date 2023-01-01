from name_function import get_formated_name

print('Enter q to quit')
while True:
    first = input('\nEnter first name: ')
    if first == 'q':
        break
    last = input('Enter last name: ')
    if last == 'q':
        break
    print(get_formated_name(first, last))
