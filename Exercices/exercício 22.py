name = str(input('Enter a name:'))

#Total uppercase
print(name.upper())

#Total lowercase
print(name.lower())

#No espaces
print(len(name)-name.count(' '))


#Divided
print(name.split())
fn = name.split()
print(len(fn[0]))

#or
print(name.find(' '))

