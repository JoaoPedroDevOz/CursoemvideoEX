products = ('Mouse', 60.90, 'Mouse Pad', 15.90, 'Teclado', 150, 'Monitor', 400, 'Placa de vídeo', 1050, 'CPU', 600)

print('-'*40)
print(f"{'Store price':^40}")
print('-'*40)



for itens in range(len(products)):
    if itens % 2 == 0:
        print(f'{products[itens]:.<30}', end='')
    elif itens % 2 == 1:
        print(f'R$ {products[itens]:.2f}')
print('_'*40)
