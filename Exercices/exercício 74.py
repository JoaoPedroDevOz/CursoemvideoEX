from random import randint
cont = big = low = 0


'''while cont <= 4:
    x = randint(0, 100)
    cont += 1
    tuple = f'{x}'
    print(tuple, end=' ')
    if cont == 1:
        big = low = tuple
    else:
        if tuple > big:
            big = tuple
        if tuple < low:
            low = tuple
print(f'\nThe bigger number is {big}\nThe smaller number is {low}')'''

numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) )
print(f'The sorted values is ', end='')
for num in numbers:
    print(f'{num}', end=' ')
print(f'\nThe bigger number is {max(numbers)}\nThe smaller number is {min(numbers)}')
