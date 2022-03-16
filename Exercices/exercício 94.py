people = dict()
group = list()
sum = average = 0

while True:
    people.clear()
    while True:
        people['name'] = str(input('Name: ')).capitalize()
        people['age'] = int(input('Age: '))
        people['sex'] = str(input('Sex: [M/F] ')).upper()
        if people['sex'] not in 'MF':
            print('Please, only [M/F] ')
            people['sex'] = str(input('Sex: [M/F] ')).upper()
        else:
            break
    sum += people['age']
    group.append(people.copy())

    ask = str(input('Do you wanna continue? [Y/N] ')).upper()[0]

    if ask not in 'YN':
        ask = str(input('Do you wanna continue? [Y/N] ')).upper()[0]
    else:
        if ask == 'N':
            break

print(group)
print()
print(f"There are {len(group)} people registered.\n")
average = sum / len(group)
print(f'The average between ages is {average:5.1f}.\n')
print(f'The women registered was: ')

for g in group:
    if g['sex'] == 'F':
        print(f'{g["name"]}', end=' \n')
print()
print('The people that are over average: ')
for g in group:
    if g['age'] >= average:
        print(f'{g["name"]}')


