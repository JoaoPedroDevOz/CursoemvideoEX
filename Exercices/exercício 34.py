sal = float(input('How much is the salary: R$'))

a1 = (sal*10)/100
a1t = a1 + sal

a2 = (sal*15)/100
a2t = a2 + sal

if sal >=1.250:
    print('The salary increase will be from R$ {}, being a totally R$ {:.2f}. '.format(a1, a1t))
else:
    print('The salary increase will be from R$ {}, being a totally R$ {}'.format(a2, a2t))

#or

if sal <= 1.250:
    novo = sal + (sal * 15/100)
else:
    novo = sal + (sal * 10/100)
print('The salary increase will be from R$ {}, being a totally R$ {}'.format(sal, novo))