sum = 0
cont = 0

for x in range(0, 6):
    num = int(input('Enter a number:'.format(x)))
    if num % 2 == 0:
        sum += num
        cont += 1
print('You said {} numbers and the total sum is {}'.format(cont, sum))