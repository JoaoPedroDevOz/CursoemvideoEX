alg = int(input('How many days rented?'))
km = int(input('How many kilometers traveled?'))

pagamento = (alg * 60) + (km * 0.15)

print('The total to pay is R${:.2f}'.format(pagamento))