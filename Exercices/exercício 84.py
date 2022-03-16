lista = list()
lprinc = list()
big = low = 0


while True:
    lista.append(str(input('Enter a name: ')))
    lista.append(float(input("What's the weight? ")))
    ask = str(input('Do you want to continue? [Y/N] ')).upper()

    if len(lprinc) == 0:
        lista[1] = big = low
    else:
        if lista[1] > big:
            big = lista[1]
        if lista[1] < low:
            low = lista[1]

    lprinc.append(lista[:])
    lista.clear()

    while ask not in 'YN':
        ask = str(input('Do you want to continue? [Y/N] ')).upper()
    else:
        if ask == 'N':
            break

print(f'Were {len(lprinc)} people registered.')

for p in lprinc:
    if p[1] == big:
        print(f'The heaviest people is {p[0]}')

for p in lprinc:
    if p[1] == low:
        print(f'The lightest people is {p[0]}')




