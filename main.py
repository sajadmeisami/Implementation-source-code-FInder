import random


a = int(input('Enter a number= '))
i=0
while i==0:
    b = random.randint(1, 100)
    if (b - a) > 0:
        print('Bozorgtar')
    elif (b - a) < 0:
        print('koochektar')
    else:
        print('Afarin dorosteh')
        i=i+1


