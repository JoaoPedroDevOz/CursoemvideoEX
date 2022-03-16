x = str(input('Enter a word:')).lower()
if x == x[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
x = ''.join(x.split())
print(x + x[::-1])

