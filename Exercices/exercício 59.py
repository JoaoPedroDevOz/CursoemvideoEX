import time

ask = int

while ask !=5:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a number: "))

    print('''
    [1] - sum
    [2] - multiply
    [3] - bigger
    [4] - new numbers
    [5] - exit the program
    ''')
    ask = int(input('Enter a follow alternatives: '))

    big = n1

    if ask == 1:
        print(n1+n2)
    elif ask == 2:
        print(n1*n2)

    elif ask == 3:
        if n2 > big:
            big = n2
            print(big)
        else:
            print(big)
    elif ask == 4:
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter a number: "))

        print('''
        [1] - sum
        [2] - multiply
        [3] - bigger
        [4] - new numbers
        [5] - exit the program
        ''')
        ask = int(input('Enter a follow alternatives: '))
    elif ask == 5:
        print('Finishing...')
        time.sleep(3)
print('Check back often')
