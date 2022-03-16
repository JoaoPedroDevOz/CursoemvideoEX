words = ('Study', 'Mouse', 'Mouse pad', 'Key board', 'Aprender', 'Musica', 'Vida', 'Programar')


for w in words:
    print(f'\nIn word {w} we have:', end='')
    for vogais in w:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')



