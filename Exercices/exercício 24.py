n1 = str(input('Enter the name of the you live:')).strip()

s = n1.upper()
print('SANTO' in s)

#or

n2 = str(input('Enter the name of the you live:')).strip()
print(n2[:5].upper() == 'SANTO')