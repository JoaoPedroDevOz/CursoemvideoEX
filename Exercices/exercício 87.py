matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even = big = segl = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Enter a number to the position [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            even += matriz[l][c]
    print()
print(f'The sum of whole even numbers is {even}.')

for l in range(0, 3):
    segl += matriz[l][2]

print(f'The sum of whole numbers in third column is {segl}.')

for c in range(0, 3):
    if c == 0:
        big = matriz[1][c]
    elif matriz[1][c] > big:
        big = matriz[1][c]
print(f'The biggest number of the second line is {big}.')