n = cont = s = 0


while n != 999:
    n = int(input('Enter a number: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'The sum of all values is {s} and the quantity of values typed is {cont}')