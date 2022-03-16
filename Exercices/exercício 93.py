ficha = dict()
gols = list()
cont = 0

ficha['Name'] = str(input('Name of the player: '))
ficha['Matches'] = int(input(f'How many {ficha["Name"]} matches played? '))
print()
print('How many gols he did:')
for x in range(0, ficha['Matches']):
    cont += 1
    gols.append(int(input(f'Match {cont}: ')))
    ficha['total'] = sum(gols)
    if ficha['Matches'] == cont:
        break
ficha['Gols'] = gols[:]
print('-=' * 30)
for cont, item in ficha.items():
    print(f'{cont}: {item}')
print('-=' *30, '\n')
print(ficha, '\n')
print('-=' * 30)

print(f'{ficha["Name"]} played {len(ficha["Gols"])} matches.')
for i, v in enumerate(ficha['Gols']):
    print(f'    => Match {i}: {v} gols.')
print(f'Total: {ficha["total"]} gols')
