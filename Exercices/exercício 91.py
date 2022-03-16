from random import randint
from time import sleep
from operator import itemgetter

cont = 0

jog = {'Jogador 1 ': randint(1, 6),
       'Jogador 2 ': randint(1, 6),
       'Jogador 3 ': randint(1, 6),
       'Jogador 4 ': randint(1, 6)}

ranking = list()

for jogadores, result in jog.items():
    print(f'The {jogadores}had result {result}')
    sleep(0.5)
ranking = sorted(jog.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('{:^20}'.format('RANKING'))
for i, v in enumerate(ranking):
    print(f'{i+1}° place: {v[0]} with {v[1]}.')
    sleep(0.5)
