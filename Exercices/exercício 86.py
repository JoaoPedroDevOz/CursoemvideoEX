matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = list()

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Enter a number to the position [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()





