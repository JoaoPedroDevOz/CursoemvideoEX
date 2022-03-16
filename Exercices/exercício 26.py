n1 = str(input('Enter a word:')).lower().strip()

print("'a' show {} times".format(n1.count('a')))
print("The first 'a' show in position {}".format(n1.find('a')+1))
print("The last 'a' show in position {}".format(n1.rfind('a')))