num = (int(input('Enter a number: ')),
    int(input('Enter a number: ')),
    int(input('Enter a number: ')),
    int(input('Enter a number: ')))

print(f'The values typed are {num}', end=' ')

print(f'The value 9 showed {num.count(9)} times')
if 3 in num:
    print(f'The value 3 showed in position {num.index(3)+1}°')
else:
    print("There's nothing 3 in any position.")
for n in num:
    if n %2 == 0:
        print(f'The even numbers are {n}')



