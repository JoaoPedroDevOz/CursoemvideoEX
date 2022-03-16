from random import randint
import time
str = "Let's Play Mega Sena!!!"
print('-='*30)

print("{:^60}".format(str))
print('-='*30)


lista = list()
ask = int(input('Do you want to sort how many games? '))
cont = 0
games = list()

for i in range(0, ask):
    cont += 1
    while len(lista) != 5:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        if len(lista) == 6:
            break
    games.append(lista[:])
    lista.clear()
    print(f'Game {cont}: {games}')
    time.sleep(0.8)
    games.clear()


#Or

'''
quant = int(input('Do you want to sort how many games? '))
lista = list()
jogos = list()
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1)
print('-='*5, '< Boa sorte >', '-='*5)
'''