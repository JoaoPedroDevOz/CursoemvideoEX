#multiplos de três ímpares
sum = 0
cont = 0

for x in range(1, 501):
    if x %2 == 1 and not x%3: #and not para encontrar multiplo de 3; se fosse independente seria if not.
        print(x)
        sum = sum + x
        cont = cont + 1
print('The sum of all {} values solicited is {}'.format(cont, sum))
