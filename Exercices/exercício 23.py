n1 = int((input('Enter a number between 0 and 9999:')))

#better

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print('Unity: {}\nTen: {}\nHundred: {}\n Thousand: {}'.format(u, d, c, m))

#other

n2 = int((input('Enter a number between 0 and 9999:')))

div = n2.split()

for i in n2:
    div.append(i)

print(div)
print('Unity: {}\nTen: {}\nHundred: {}\nThousand: {}'.format(div[1], div[2], div[3], div[4]))
