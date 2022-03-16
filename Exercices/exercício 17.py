import math

cato = float(input('Whats the size of the opposite leg?'))
cata = float(input('Whats the size of the adjacent collar?'))

hip = (cato**2) + (cata**2)

vhip = math.sqrt(hip)

#with hypt

hip2 = math.hypot(cato, cata)

print('{:.2f}'.format(vhip))
print('{:.2f}'.format(hip2))