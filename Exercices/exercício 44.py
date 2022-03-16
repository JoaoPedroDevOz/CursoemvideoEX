print('{:^40}'.format('TECHMOON'))

produto = float(input('How much cost the product? R$'))

print('''
[1] - In cash (money/ check) - 10% off
[2] - In cash on card - 5% off
[3] - 2x on card - Normal price
[4] - 3x or more on card - 20% interest
''')

ask = str(input('How will pay? '))

if ask == '1':
    total = produto - (produto * 10/100)
    print('The total value is {}'.format(total))

elif ask == '2':
    total = produto - (produto * 5/100)
    print('The value is {}'.format(total))

elif ask == '3':
    total = produto
    parcela = total/2
    print('The value is {} and the installment amount is {}'.format(produto, parcela))

elif ask == '4':
    total = produto + (produto * 20/100)
    top = int(input('How many installments? '))
    parcela = total/top
    print('The value is {} and the installment amount is {}'.format(total, parcela))

