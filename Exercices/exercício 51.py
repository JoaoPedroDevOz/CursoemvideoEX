p = int(input('First term: '))
r = int(input('Reason: '))
d = p + (10 - 1)*r

for x in range(p, d + r, r):
    print(x, end=" -> ")


