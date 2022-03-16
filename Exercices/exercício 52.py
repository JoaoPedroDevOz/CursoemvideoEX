x = int(input('Enter a number:'))

if x > 1 and x%1 == 0 and x%x == 0:
    print("It's a prime number")
else:
    print("It's not a prime number")