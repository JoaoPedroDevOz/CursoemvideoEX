idade = int(input('How old are you? '))

menos = 18 - idade
mais = idade - 18

if idade == 18:
    print("\033[33mIt's the time to be recruited!\033[m")
elif idade < 18:
    print("\033[1;32mIt's not the time to be recruited! There's still {} years to introduce yourself.\033[m".format(menos))
elif idade > 18:
    print("\033[1;31mIt's high time to be recruited!!! Was {} years to introduce yourself. Come on!\033[m".format(mais))