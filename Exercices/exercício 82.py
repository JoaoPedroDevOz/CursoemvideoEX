listaeven = list()
listaodds = list()
lista = list()

while True:
    n = int(input('Enter a number: '))

    lista.append(n)

    while n in lista:
        if n % 2 == 0:
            listaeven.append(n)
        if n % 2 == 1:
            listaodds.append(n)
        break



    ask = str(input('Do you want to continue? [Y/N] ')).upper()

    while ask not in 'YN':
        if ask not in 'YN':
            print('Try again')
            ask = str(input('Do you want to continue? [Y/N] ')).upper()

        if ask in 'YN':
            break
    if ask == 'N':
        break

print(lista)
print(f'The evens numbers are {listaeven}')
print(f'The odds numbers are {listaodds}')

'''while True:
    n = int(input('Enter a number: '))

    lista.append(n)

    ask = str(input('Do you want to continue? [Y/N] ')).upper()
    
    if ask == 'N':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        listaeven.append(v)
    if v % 2 == 1:
        listaodds.append(v)
        
print(lista)
print(f'The evens numbers are {listaeven}')
print(f'The odds numbers are {listaodds}')'''