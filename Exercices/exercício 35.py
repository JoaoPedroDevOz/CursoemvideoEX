print('\033[35m-=\033[m' *20)
print('\033[4;35mAnalyse Triangles\033[m')
print('\033[35m-=\033[m' *20)

a = int(input('\033[1;32mEnter the length of a line number one:\033[m'))
b = int(input('\033[1;33mEnter the length of a line number two:\033[m'))
c = int(input('\033[1;34mEnter the length of a line number three:\033[m'))

if a < b + c and b < a + c and c < b + a:
    print('\033[1;32mCan form a triangle\033[m')
else:
    print("\033[1;31mCan't form a triangle, sorry\033[m")