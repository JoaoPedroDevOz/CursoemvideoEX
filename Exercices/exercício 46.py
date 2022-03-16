from time import sleep
import emoji



for x in range(10, 0, -1):
    print(x)
    sleep(1)#alternancia entre numero e sleep de 1 segundo
print("BOOM", emoji.emojize(":kissing:", use_aliases=True))