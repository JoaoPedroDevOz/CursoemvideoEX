sumage = 0
medage = 0

mage = 0
nameold = ''

totw = 0
totage = 0

for x in range(1, 5):
    name = str(input("What's your name?"))
    age = int(input("How old are your?"))
    sex = str(input("What's your sex? [M/F]: ")).upper()
    sumage += age #0 += totaldeidades
    totage += age/age #total de idades
    if sex in 'M' and age > mage:
        mage = age #0 = se age for maior que mage, então mage recebe o valor de age
        nameold = name #'' = troca de nome conforme as condições
    if sex in 'F' and age < 20:
        totw += 1 #0 += 1 - para cada mulher dentro do if
medage += sumage/totage #0 += totaldeidades/4

print('The media between the ages is {}'.format(medage))
print('The age of the oldest guys is {} and your name is {}'.format(mage, nameold))
print('The total of women with 20 years less are {}'.format(totw))


