import math

while True:
    ask = int(input("Enter a number: "))
    print(math.factorial(ask))
    break
#or


number = int(input("Enter a number: "))

result = 1
count = 1

while count <= number:
    result *= count
    count += 1
print(result)

#or

n = int(input('Enter a number: '))
c = n
f = 1

while c > 0:
    print('{}!'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f*=c
    c -= 1
print(f, end='''\n''')

#for

ct = 1

num = int(input("Enter a number: "))

for num in range(1, num+1):
    ct *= num
    print(ct)
