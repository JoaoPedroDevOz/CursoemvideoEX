lista = list()

while True:
    n = int(input('Enter a number: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Try again, please')

    ask = str(input('Do you want to continue? [Y/N] ')).upper()

    while ask not in 'YN':
        print('Try again, please')
        ask = str(input('Do you want to continue? [Y/N] ')).upper()

        if ask in 'YN':
            break
    if ask == 'N':
        break

print(lista)

