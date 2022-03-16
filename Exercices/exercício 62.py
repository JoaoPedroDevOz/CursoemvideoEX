p = int(input('First term: '))
r = int(input('Reason: '))
t = p
cont = 1
total = 0
more = 10

while more != 0:
    total += more
    while cont <= total:
        print('{} -> '.format(t), end='')
        t += r
        cont += 1
    print('Pause', end='')
    more = int(input('\nHow many numbers do u want show? '))
    if more == 0:
        break

print('Finish. Has {} terms'.format(cont-1))
