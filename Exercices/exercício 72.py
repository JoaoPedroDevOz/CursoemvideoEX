from num2words import num2words

n1 = 0

extenso = ('Zero', 'One', 'Two', 'Three',  'Four', 'Five',
            'Six', 'Seven', 'Eight',  'Nine',  'Ten',
            'Eleven', 'Twelve',  'Thirteen', 'Fourteen', 'Fifteen',
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')


while True:
    n1 = int(input('Enter a number between 0 and 20 or 999 to finish: '))
    if 0 <= n1 <= 20:
        print('\n The number write is')
        print('-='*20)
        print(f'{extenso[n1]}')
        print('-='*20, '\n')

    elif n1 == 999:
        print('End, BaBai.')
        break
    else:
        print('Try again')
