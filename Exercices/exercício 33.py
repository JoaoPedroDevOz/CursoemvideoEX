a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
c = int(input('Enter a number:'))

smal = c
if a<b and a<c:
    smal = a

if b<a and b<c:
    smal = b

print('The smaller value is {}'.format(smal))

big = c
if a>b and a>c:
    big = a
if b>a and b>c:
    big = b

print('The bigger value is {}'.format(big))