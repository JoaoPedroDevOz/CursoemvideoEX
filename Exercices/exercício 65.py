quantask = quantnum = bigger = lower = 0
ask = int
keep = str

while keep != 'No':
    ask = int(input('Enter a number:'))
    keep = str(input('Do you wanna keep going? [Yes/ No]')).capitalize()
    quantask += 1
    quantnum += ask

    if quantask == 1:
        bigger = lower = ask
    else:
        if ask > bigger:
            bigger = ask
        if ask < lower:
            lower = ask
    if keep == 'Yes':
        ask = int(input('Enter a number:'))
    elif keep == 'No':
        break
media = quantnum/quantask

print('The media of the values is {:.2f} '.format(media))
print('The bigger value is {} and the lower value is {}'.format(bigger, lower))
