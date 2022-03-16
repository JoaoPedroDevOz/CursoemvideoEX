from datetime import date

anat = date.today().year

ano = int(input('Enter the year of birth: '))

idade = anat - ano

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <=19:
    print('Junior')
elif 19 < idade <=25:
    print('Sênior')
else:
    print('Master')