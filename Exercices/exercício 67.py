cont = 0
n = 0


while n > 0:
    n = int(input('Do you want to see the table of what value? '))
    while cont <= 10:
        print(f'{n} x {cont} = {n*cont}')
        cont +=1

    if n < 0:
        print("Sorry, but negatives numbers don't are utilized for")
        break