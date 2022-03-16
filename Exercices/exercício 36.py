print('\033[4;36mSimulator buy house\033[m')

e = float(input("\033[32mHouse's value: R$"))
s = float(input('Costumer salary: R$'))
a = float(input('How many years will pay:\033[m'))

m = e/(a*12)
n = s * 30/100

if n and m < 10:
    print("You'd have to pay R${:.2f} for month, and the minimum that you can make an financing is R${}".format(m * 1000, n * 1000))
else:
    print("You'd have to pay R${:.2f} for month, and the minimum that you can make an financing is R${}".format(m, n))
if e/(a*12) < s*0.3:
    print('\033[1;37mYou\033[m \033[32mcan\033[m \033[1;37mbuy this house, well pleasure!\033[m')
else:
    print("\033[1;37mYou\033[m \033[31mcan't\033[m \033[1;37mbuy this house, sorry. Try other\033[30m")