def get_formated_name(first, last, middle = ''):
    if middle:
        full_name = f'{first.title()} {middle.title()} {last.title()}'
    else:
        full_name = f'{first.title()} {last.title()}'
    return full_name