peso = float(input("What's your weight? "))
altura = float(input("What's your height? "))

imc = peso / (altura ** 2)

print('Your imc is {:.2f}kg/m2.'.format(imc))

if imc < 18.5:
    print('Under weight')
elif 18.5 < imc < 25:
    print('Ideal weight')
elif 25 < imc < 30:
    print('Overweight')
elif 30 < imc < 40:
    print('Obesity')
else:
    print('morbid obesity')