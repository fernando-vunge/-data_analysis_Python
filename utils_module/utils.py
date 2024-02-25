def ln(lenght=50):
    for i in range(1,lenght): print('-', end='')
    print('')

def column(items):
    line_size = len_longer(items)
    for item in items:
        ln(lenght = (line_size + 2))
        print(item)
    ln(lenght = (line_size + 2))

def len_longer(items):
    len_longer = 0
    for item in items:
        len_item = len(str(item))
        if len_item > len_longer:
            len_longer = len_item
    return len_longer