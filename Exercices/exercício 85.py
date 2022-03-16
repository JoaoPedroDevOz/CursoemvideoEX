lista = [[], []]
cont = 0

for i in range(0, 7):
    cont = int(input('Enter a number: '))

    if cont % 2 == 1:
        lista[0].append(cont)

    else:
        lista[1].append(cont)

print(f'The even numbers are {sorted(lista[0])}')
print(f'The odd numbers are {sorted(lista[1])}')

