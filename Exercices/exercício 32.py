from datetime import date

ano = int(input('\033[4;36mEnter a year to know if is a leap year:\033[m'))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print('{}{}{} \033[32mis a leap Year\033[m'.format('\033[1;30m', ano, '\033[m'))
else:
    print("{}{}{} \033[31main't a leap year\033[m".format('\033[1;30m', ano, '\033[m'))