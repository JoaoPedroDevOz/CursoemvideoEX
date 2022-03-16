sex2 = str(input("What's your sex: [M/F] ")).upper()[0].strip()

while sex2 == 'M' or 'F':
    if sex2 == 'M':
        print('sex {} successfully registered'.format(sex2))
        break
    elif sex2 == 'F':
        print('Sex {} successfully registered'.format(sex2))
        break
    else:
        print('Invalid')
        sex2 = str(input("What's your sex: [M/F] ")).upper()

