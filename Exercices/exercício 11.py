n1 = int(input("width wall:"))
n2 = int(input("Height wall:"))

print('{},{}'.format(n1, n2))

area = n1*n2

print("The wall's area is {} m²".format(area))

paint = area/2

print('Need {:.2f} liters of paint.'.format(paint))