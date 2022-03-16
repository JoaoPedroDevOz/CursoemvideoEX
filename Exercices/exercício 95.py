ficha = dict()
match = list()
time = list()

while True:
    ficha.clear()
    ficha['Name'] = str(input('Name of the player: ')).capitalize()
    total = int(input(f'How many {ficha["Name"]} matches played? '))
    match.clear()
    for x in range(0, total):
        match.append(int(input(f'How many gols he did in match {x+1}? ')))
    ficha['Gols'] = match[:]
    ficha['total'] = sum(match)
    time.append(ficha.copy())
    while True:
        ask = str(input('Do you wanna continue? [Y/N] ')).upper()[0]
        if ask in 'YN':
            break
        print('Only [Y/N]')
    if ask == 'N':
        break

print('-' * 30)
print('cod ', end='')
for i in ficha.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for k, j in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    search = int(input('To show the code of any player, type the code: (999 to break)'))
    if search == 999:
        break
    if search >= len(time):
        print(f"There's not exist this player code {search}.")
    else:
        print(f'Data of player {time[search]["Name"]}: ')
        for i, g in enumerate(time[search]["Gols"]):
            print(f'   In game {i+1} did {g} gols.')
    print('-=' * 40)
print('<<SEE LONG>>')