# Bonusuppgift 2, GPP101

# Definiera brädans startpositioner

board = [[' 2','13',' 5','14'],
         [' 8',' 7','10',' 9'],
         [' 1','11',' 4',' 6'],
         ['15',' 3','12','##']]
x = 3 # x position of empty ('##') position
y = 3 # y position of empty ('##') position

print("Enter your next move by using 'w,a,s,d' for up,down,left,right. 'q' is for quit.")
key = '*'
while key != 'q':
    for line in board:  # Print the board
        print('|',*line,'|')
    print('')
    key = input("Enter next move (w,a,s,d or q): ")

    #Flytta den tomma rutan åt vänster 
    if key == 'a':
        if y <= 0:
            y = 0
        else:
            board[x][y], board[x][y-1] = board[x][y-1], board[x][y]
            y = y - 1

    #Flytta den tomma rutan åt höger
    elif key == 'd':
        if y >= 3:
            y = 3
        else:
            board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
            y = y + 1

    #Flytta den tomma rutan uppåt
    elif key == 'w':
        if x <= 0:
            x = 0
        else:
            board[x][y], board[x-1][y] = board[x-1][y], board[x][y]
            x = x - 1

    #Flytta den tomma rutan neråt
    elif key == 's':
        if x >= 3:
            x = 3
        else:
            board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
            x = x + 1

    # Avsluta programmet
    elif key == 'q':
        print('')
        print("Bye, see you soon!")
        quit()

    # Rätta användaren om den väljer ett ogiltigt alternativ
    else:
        print('')
        print('Välj ett korrekt alternativ.')
        print('')