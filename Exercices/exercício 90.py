nota = {'nome': str(input('Name: ')).capitalize(), 'Average': float(input('Average: '))}

for cont, item in nota.items():
    print(f'{cont} is {item}')
if nota["Average"] < 5:
    print(f'The student {nota["nome"]} was Reproved.')
if 5 <= nota["Average"] < 7:
    print(f'The student {nota["nome"]} is in Recovery.')
if nota["Average"] >= 7:
    print(f'The student {nota["nome"]} was Approved.')
