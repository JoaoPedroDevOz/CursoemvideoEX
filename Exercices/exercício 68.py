print('-='*12)
print(str("Let's play even and odds").upper())
print('-='*12)

from random import randint

com = randint(1, 10)

cont = 0
jogador = True

while not jogador == False:
    jog = int(input('Enter a value: '))
    ask = str(input('EVEN or ODD? [E/O] ')).upper()

    sum = jog + com

    print('-' * 20)
    print(f'You choice {jog} and the computer choice {com}\nThe sum between the numbers is {sum}')
    print('-' * 20)

    if sum % 2 == 0:
        if ask == 'E':
            cont += 1
            print("You're the Winner")
            print('We go again...')
            print('-=' * 12)
        if ask == 'O':
            print("You lose")
            print('-=' * 12)
            break
    elif sum % 2 == 1:
        if ask == 'E':
            print("You lose")
            print('-=' * 12)
            break
        if ask == 'O':
            cont += 1
            print("You're the Winner")
            print('We go again...')
            print('-=' * 12)

print(f'GAME OVER! You won after {cont} turns')
