print('-='*10, '{:^10}'.format('Multiplicantion table'), '-='*10)

c = int(input('Enter a number: '))

for x in range(1, 11):
    print('{} * {} = {}'.format(c, x, c*x))