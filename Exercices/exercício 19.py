import random

n1 = str(input('Enter a name:'))
n2 = str(input('Enter a name:'))
n3 = str(input('Enter a name:'))
n4 = str(input('Enter a name:'))

l = (n1, n2, n3, n4)
sort = random.choice(l)

print('Who was dranw was:', sort)