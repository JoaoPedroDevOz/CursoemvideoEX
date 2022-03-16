nome = 'TECH LIFE'

print("-="*15)
print("{:^30}".format(nome))
print("-="*15)

total = thous = lower = cont = 0
cheap = ''
while True:
    prod = str(input("Product's name: ")).capitalize()
    price = float(input("Product's price: R$ "))

    ask = str(input("Do you want continue? [Y/N] ")).upper().strip()[0]

    total += price
    cont += 1

    if price > 1000:
        thous += 1

    if cont == 1 or price < lower:
        lower = price
        cheap = prod

    if ask == 'N':
        break
print('{:^30}'.format('Finish'))
print(f"The total spent is: R$ {total}.")
print(f"{thous} products cost spent over R$ 1.000.")
print(f"{cheap} is the product cheapest price that cost {lower}")



