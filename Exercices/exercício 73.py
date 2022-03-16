times = ('America mg', 'Athletico pr', 'Atletico go', 'Atletico mg', 'Avai', 'Botafogo', 'Ceara sc', 'Corinthians', 'Coritiba', 'Cuiaba',
'Flamengo', 'Fluminense', 'Fortaleza', 'Goias', 'Internacional', 'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'Sao Paulo')


timesorig = ('América-MG', 'Athlético-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Ceará SC', 'Corinthians','Coritiba', 'Cuiabá',
'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo')

n = 1

print('='*40)
print(f"{'Teams list':^40}")
print('='*40)

for t in timesorig:
    print(t, end=' ')

while n != 0:
    while n <=4:
        print('\n1 - Only top 5.\n2 - Only last 4.\n3 - Alphabetic order.\n4 - What position is Some team.\n0 - To finish the program.')
        n = int(input('Enter a number between 1 and 4 to show the following thing: '))

        if n == 1:
            print(f'{timesorig[:5]}')
        elif n == 2:
            print(f'{timesorig[-4::]}')
        elif n == 3:
            print(sorted(timesorig))
        elif n == 4:
            print('América MG', 'Athlético PR', 'Atlético GO', 'Atlético MG', 'Avaí','\n' 'Botafogo', 'Ceará SC', 'Corinthians','Coritiba', 'Cuiabá',
                    '\n''Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', '\n''Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo')
            team = str(input('Which team do you want know the position? ')).capitalize()
            if team == 'Sao paulo':
                print('This time is in position 20')
            else:
                print(f'This time is in position {times.index(team)}°')
        elif n == 0:
            break