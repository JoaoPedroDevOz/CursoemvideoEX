n = int(input('Enter a number: '))

t1 = 0
t2 = 1
cont = 0

while cont <= n:
    t3 = t1 + t2
    cont += 1
    print('{}'.format(t3), end=' -> ')
    t1 = t2
    t2 = t3
print('FIM')