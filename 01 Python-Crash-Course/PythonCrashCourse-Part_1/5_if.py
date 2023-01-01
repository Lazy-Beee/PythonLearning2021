fruit_available = ['apple', 'banana', 'pear']
ordered = ['apple', 'pear', 'banana', 'peach']
out_of_apple = False
out_of_banana = True
out_of_pear = False

for fruit in ordered:
    if out_of_apple and fruit == 'apple':
        print(f'Sorry, we are out of {fruit} right now.')
    elif out_of_banana and fruit == 'banana':
        print(f'Sorry, we are out of {fruit} right now.')
    elif out_of_pear and fruit == 'pear':
        print(f'Sorry, we are out of {fruit} right now.')
    elif fruit not in fruit_available:
        print(f"Sorry, we don't offer {fruit} in our shop")
    else:
        print(f'{fruit.title()} added to order')
