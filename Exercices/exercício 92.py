from datetime import datetime

ficha = dict()
ficha['name'] = str(input("Name: "))
born = int(input("Year of birth: "))
ficha['age'] = datetime.now().year - born
ficha['ctps'] = int(input("Work Card: (if haven't, type 0) "))
if ficha['ctps'] != 0:
    ficha['year of hire'] = int(input('Hired year: '))
    ficha['salary'] = float(input('Salary: R$'))
    ficha['retirement'] = ficha['age'] + ((ficha['year of hire'] + 35) - datetime.now().year)

for cont, item in ficha.items():
    print(f'{cont} is {item}')



