from datetime import date
year = date.today().year

totmaior = 0
totmenor = 0

for x in range(1, 8):
    c = int(input("What's year the {} was born? ".format(x)))
    i = year - c
    if i >= 21:
        totmaior +=1
    else:
        totmenor +=1
print('The total of people legal age are: {}'.format(totmaior))
print('The total of people underage are: {} '.format(totmenor))

