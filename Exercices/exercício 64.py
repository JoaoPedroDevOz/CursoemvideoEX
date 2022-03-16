print('-=-' * 20)
print("Let's play a game")
print('-=-' * 20)

ask = int
quantask = 0
cont = 0
print("Enter a any number. But if you want stop, enter the number: 999. ")

while ask != 999:
    ask = int(input('Enter a number:'))
    quantask += ask
    cont += 1
    if ask == 999:
        break

if ask == 999:
    print('The sum of all number is {}.'.format(quantask - 999))


#or

num = cont = sum = 0
num = int(input('Enter a number: [999 to stop]'))

while num != 999:
    sum += num
    cont += 1
    num = int(input('Enter a number: [999 to stop]\n'))
print('The sum of all {} numbers is {}.'.format(cont, sum))