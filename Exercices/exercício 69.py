m18 = quantF = quantM = 0

while True:
    print('-'*17)
    print(str('Register a person').upper())
    print('-'*17)

    age = int(input('Enter the age: '))
    sex = str(input('Enter the sex: [M/F] ')).upper()

    ask = str(input('Do you wanna continue? [Y/N] ')).upper()

    if age > 18:
        m18 += 1

    if sex == 'M':
        quantM += 1

    if sex == 'F' and age < 20:
        quantF += 1

    if ask == 'N':
        break

print(f"There are {m18} people over eighteen")
print(f"There are {quantM} men")
print(f"There are {quantF} women under twenty")

