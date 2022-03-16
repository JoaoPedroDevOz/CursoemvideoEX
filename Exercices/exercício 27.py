name = str(input('Enter the complete name:')).strip()
nm = name.split()
print(nm)
print('First name is: {}\nLast name is: {}'.format(nm[0], nm[len(nm)-1]))
