from random import randint
import time
print('''
[0] - Rock/ Pedra
[1] - Paper/ Papel
[2] - Scissors/ Tesoura
''')

n = ('Rock', 'Paper', 'Scissors')
comp = randint(0, 2)

time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')

jog = int(input('Rock, Paper and Scissors: ' ))

print('-=' *20)
print('You choose {}'.format(n[jog]))
print('The pc choices {}'.format(n[comp]))
print('-=' *20)

time.sleep(2)
if comp == 0:
    if jog == 0:
        print('A tie!')
    elif jog == 1:
        print('Damn it, i let you win')
    elif jog == 2:
        print('You lose, sucker. HAHAHA')
    else:
        print('Invalid')
if comp == 1:
    if jog == 0:
        print('You lose, sucker. HAHAHA')
    elif jog == 1:
        print('A tie!')
    elif jog == 2:
        print('Damn it, i let you win')
    else:
        print('Invalid')
if comp == 2:
    if jog == 0:
        print('Damn it, i let you win')
    elif jog == 1:
        print('You lose, sucker. HAHAHA')
    elif jog == 2:
        print('A tie!')
    else:
        print('Invalid')




