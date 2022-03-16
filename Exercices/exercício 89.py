ficha = list()
ask = ''



while ask != 'N':
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    ask = str(input('Do you want to continue? [YN] ')).upper()
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    while ask not in 'YN':
        ask = str(input('Do you want to continue? [YN] ')).upper()
        if ask == 'N':
            break

print('-='*30)
print('{}{:^10}{:^18}'.format('No.', 'Nomes', 'Médias'))
print('-='*30)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10}{a[2]:>8.1f}')

while True:
    opc = int(input('Do you wanna see the notes about which student? (999 to break.) '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notes by {ficha[opc][0]} are {ficha[opc][1]}')
print('Back again')












#Only


'''
lista = list()
ask = ''
n = 3
cont = 0

while ask != 'N':
    lista.append(str(input('Enter a name: ')))
    lista.append(float(input('Note 1: ')))
    lista.append(float(input('Note 2: ')))

    ask = str(input('Do you want to continue? [YN] ')).upper()

    while ask not in 'YN':
        ask = str(input('Do you want to continue? [YN] ')).upper()
        if ask == 'N':
            break

for l in range(0, len(lista), n):
    cont += 1
    print(f'{cont}' , end='')
    print(f' {lista[l: n]}', '\n', end='')
    n += 3
'''













