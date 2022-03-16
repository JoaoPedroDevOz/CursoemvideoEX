p = int(input('First term: '))
r = int(input('Reason: '))
d = p + (10 - 1)*r

s = p+r

print(p)
print(s)

while s < d:
    s += r
    print(s)


#better

t = p
cont = 1

while cont <= 10:
    print('{} -> '.format(p), end='')
    p += r
    cont +=1
print('END')
