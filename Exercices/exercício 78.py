lista = []
big = low = 0
for num in range(0, 5):
    lista.append(int(input('Enter a number: ')))

    if num == 1:
        big = low = lista[num]
    else:
        if lista[num] > big:
            big = lista[num]
        if lista[num] < low:
            low = lista[num]

print(lista)
print(f'The bigger value is {big} in position {lista.index(big)}\nThe smaller value is {low} in position {lista.index(low)}')