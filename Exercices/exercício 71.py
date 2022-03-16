print('='*20)
print('{:^20}'.format('BANK CENTER'))
print('='*20)

value = int(input("How much money do you want withdraw? R$"))
total = value

ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'There are {totced} ballot of R${ced} to R${value}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-='*15)
print('{:^30}'.format('So long. BYE!'))


