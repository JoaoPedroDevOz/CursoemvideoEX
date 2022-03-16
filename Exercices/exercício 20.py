from random import shuffle
n1 = input('Enter a name:')
n2 = input('Enter a name:')
n3 = input('Enter a name:')
n4 = input('Enter a name:')

list = [n1, n2, n3, n4]

shuffle(list)

print('The order of presentation is:{}'.format(list))
