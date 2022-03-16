n1 = int(input('Enter a number: '))
n2 = int(input('Enter other number: '))

if n1 < n2:
    print('\033[33m{}\033[m is bigger than \033[32m{}\033[m'.format(n2, n1))
elif n1 > n2:
    print('\033[33m{}\033[m is bigger than \033[32m{}\033[m'.format(n1, n2))
else:
    print('\033[33m{}\033[m and \033[32m{}\033[m is equal'.format(n2, n1))