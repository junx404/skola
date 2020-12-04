#!/bin/python3
from turtle import *
title('Julprogram')

while True:
    print('*' * 30)
    print('1. Pepparkaksfigur')
    print('2. Julstjärna')
    print('X. Avsluta programmet')
    print('*' * 30)
    print(' ')
    val = input('Välj alternativ: ',).lower()

# Pepparkaksfigur, stjärna
    if val == '1':
        clear()
        penup()
        goto(0,100)
        pendown()
        goto(30,30)
        goto(120,20)
        goto(50,-20)
        goto(85,-100)
        goto(0,-50)
        goto(-85,-100)
        goto(-50,-20)
        goto(-120,20)
        goto(-30,30)
        goto(0,100)

# Julstjärna

    elif val == '2':
        clear()
        tagg = input('Hur många taggar ska stjärnan ha? ')
        grad = 360 // int(tagg)

        for i in range(int(tagg)):
            if i % 2 == 0:
                fd(100)
                bk(100)
                lt(grad)
            elif i % 2 == 1:
                fd(70)
                bk(70)
                lt(grad)

# Avsluta
    elif val == 'x':
        quit()

# Om användaren inte lyder

    else:
        print(' ')
        print('Välj om, välj rätt.')
        print(' ')
