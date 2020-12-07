import time

highscore = [9.99,9.99,9.99]
Spelare = ['Test','Test','Test']

def cd(t):
    while t > 0:
        print(t)
        t = t - 1
        time.sleep(0.5)

def spel():
    print(' ')
    print('*' * 44)
    print('')
    print('Försök att komma så nära 5 sekunder som möjligt. ')
    print('*' * 44)
    input('Enter startar spelet efter en kort nedräkning! ')
    cd(3)
    start = time.time()
    print(' ')
    input('Enter stoppar klockan ')
    total = time.time() - start
    diff = round(total, 2) - 5.0
    if diff < 0:
        diff = -diff

    if diff < (highscore[-1]):
        Namn = input('Skriv ditt namn: ')
        highscore.append(diff)
        Spelare.append(Namn)
        print('~~~~ Nytt rekord! ~~~~')

    elif diff < (highscore[-2]):
        Namn = input('Skriv ditt namn: ')
        highscore.insert(-1, diff)
        Spelare.insert(-1, Namn)
        print("Grattis, du hamnade på topplistan!")

    elif diff < (highscore[-3]):
        Namn = input('Skriv ditt namn: ')
        highscore.insert(-2, diff)
        Spelare.insert(-2, Namn)
        print('Grattis, du hamnade på topplistan!')
    
    print(' ')
    print('Du missade med: ', round(diff, 3))
    print('Totaltiden blev: ', round(total, 3))
    print(' ')
    scoreboard()

    spel()
    return diff, total
    


def scoreboard():
    print(' Highscore list ')
    print(' #1 ',highscore[-1],' ', Spelare[-1])
    print(' #2 ',highscore[-2],' ', Spelare[-2])
    print(' #3 ',highscore[-3],' ', Spelare[-3])

spel()