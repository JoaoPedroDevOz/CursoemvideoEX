lista = list()
cont = 0

while True:
    n = int(input('Enter a number: '))

    cont += 1

    lista.append(n)

    ask = str(input('Do you want to continue? [Y/N] ')).upper()

    while ask not in 'YN':
        if ask not in 'YN':
            print('Try again.')
            ask = str(input('Do you want to continue? [Y/N] ')).upper()

        if ask in 'YN':
            break

    if ask in 'N':
        break

print(lista)
print(f'Were typed {cont} numbers')
print(f'The reverse list stay: {lista[::-1]}')
print(f'In descending order stay {sorted(lista, reverse=True)}')

if 5 not in lista:
    print("There are not the number five in list")
else:
    print(f'There are the number five in list in position {lista.index(5)}')





