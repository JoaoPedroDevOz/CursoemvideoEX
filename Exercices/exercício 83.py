x = str(input('Enter a expression: '))

'''for caracter in x:
    x.strip()
    a = x.count('(')
    b = x.count(')')
    if a == b:
        print('This expression is correct')
        break
    else:
        print('This expression is not correct')
        break'''

pilha = []

for símb in x:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('This expression is correct')
else:
    print('This expression is not correct')