num = int(input('Enter any whole number to the conversation: '))

ask = str(input('''Choice the type of conversation
1 - Binary
2 - Octal
3 - Hexadecimal
'''))



if ask == '1':
    print(bin(num)[2:])
elif ask == '2':
    print(oct(num)[2:])
elif ask == '3':
    print(hex(num)[2:])
else:
    print('Invalid option')