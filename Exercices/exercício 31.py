ask = float(input("What's the distance in KM:"))

value1 = ask * 0.50
value2 = ask * 0.45

if ask <= 200:
    print('The value of the travel is {}'.format(value1))
else:
    print('The value of the travel is {}'.format(value2))

#or

price = ask * 0.50 if ask <= 200 else ask * 0.45

print('The price of the travel is {}'.format(price))