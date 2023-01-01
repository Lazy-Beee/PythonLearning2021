

def hello(greeting, name="Jun"):
    print(f'Hello {name}, {greeting}')


hello('nice to meet you.')
hello('how are you today?', name='Jack')


def user_sign_up(**user):
    name = input('Enter user name (enter q to quit): ')
    if name == 'q':
        return False
    else:
        age = input('Enter user age: ')
        gender = input('Enter user gender: ')
        user = {'user_name': name,
                'user_age': age,
                'user_gender': gender}
        return user


while True:
    user_file = user_sign_up()
    if not user_file:
        print('User log-in finished.')
        break
    print(f'\nUser name: {user_file["user_name"]}')
    print(f'User age: {user_file["user_age"]}')
    print(f'User gender: {user_file["user_gender"]}\n')

