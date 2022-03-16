n1 = float(input('Enter the first note: '))
n2 = float(input('Enter the second note: '))

m = (n1+n2)/2

print(m)
if m >= 7:
    print('You were approved!')
if m < 5:
    print('You were disapproved!')
if 5 < m < 7:
    print('You are in recovery!')
