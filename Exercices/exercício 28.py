import time
from random import randint

print('-=-' * 20)
print("Let's play a game")
print('-=-' * 20)

ask = int(input('Guess a number from 1 to 5:'))

sort = randint(0, 5)

print('Processing...')
time.sleep(2)

if ask == sort:
    print('DAMN IT! I lose this turn.')
else:
    print('YOU LOSE, SUCKER! HAHAHA')

print('The number drawn was {}'.format(sort))
