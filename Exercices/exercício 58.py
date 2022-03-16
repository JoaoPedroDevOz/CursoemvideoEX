from random import randint

print('-=-' * 20)
print("Let's play a game")
print('-=-' * 20)

sort = randint(0, 10)
guess = 0
correct = False

while not correct:
    ask = int(input("Guess a number from 0 to 10: "))
    guess += 1
    if ask == sort:
        correct = True
    else:
        if ask > sort:
            print('Less...Try again')
        elif ask < sort:
            print('More... Try again')
print('Correct. After {} tries, you win'.format(guess))
