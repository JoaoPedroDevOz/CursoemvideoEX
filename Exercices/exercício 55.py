maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Weight of the {}° people? ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('The biggest weight is {}Kg'.format(maior))
print("The smaller weight is {}Kg".format(menor))

