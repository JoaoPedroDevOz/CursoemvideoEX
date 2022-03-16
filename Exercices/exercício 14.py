#Celsius to Fahrenheit and Kelvin

temp = float(input("What's the temperature in C°:"))

tof = temp*1.8 + 32
tek = temp+273.15

print('The temperature in celsius {}°C for fahrenheit corresponds to {}°F and in Kelvin is {}°K.'.format(temp, tof, tek))

#Fahrenheit to Kelvin and to Celsius

tfk = (temp - 32)*5/9 + 273.15
tfc = (temp - 32)/1.8
print('The temperature in Fahrenheit {}°F for Kelvin corresponds to {:.2f}°K and to Celsius is {:.2f}°.'.format(temp, tfk, tfc))

#Kelvin to Fahrenheit and to Celsius

tkv = 1.8 * (temp - 273.15) + 32
tkc = temp - 273.15

print('The temperature in Kelvin {}°K for Fahrenheit corresponds to {:.2f}°F and to Celsius is {}°C.'.format(temp, tkv, tkc))

