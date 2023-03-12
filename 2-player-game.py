from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    # print board without numbers
    userLayout = layout
    for character in userLayout:
        if character.isnumeric():
            userLayout = userLayout.replace(character, " ")

    print(userLayout)


def movesAvailableCalc(board):
    # make list of free fields on board currently
    movesAvailable = []
    
    # Populate list with moves available as a normal list
    for i in range(rows):
        for j in range(cols):
            if board[i][j] != 'X' and board[i][j] != 'O':
                movesAvailable.append(board[i][j])
        else:
            continue
    
    return movesAvailable

def enter_move_player1(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    # Populate list with moves available as a normal list
    movesAvailable = movesAvailableCalc(board)

    # Get move from user
    userMove = int(input("Player 1 - Enter your move: "))
    while userMove not in movesAvailable:
        print("Space not available, try again")
        print("Available moves: ", movesAvailable)
        userMove = int(input("Player 1 - Enter your move: "))
        
    # Place user move into board array    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == userMove:
                board[i][j] = 'O'
                break
    
    # Place computer move on layout for output
    global layout
    for character in layout:
        if character == str(userMove):
            layout = layout.replace(character, "O")
    
    # Call to display board
    print("Player 1 move:")
    display_board(board)
    
    sign = "O"
    if victory_for(board, sign):
        print("Player 1 won!")
    elif victory_for(board, sign) == None:
        print("Game is tied")
    else:
        enter_move_player2(board)

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    # check if sign wins
    winCounter = 0
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        winCounter += 1
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        winCounter += 1
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        winCounter += 1
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        winCounter += 1
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        winCounter += 1
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        winCounter += 1
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        winCounter += 1
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        winCounter += 1
    
    if winCounter == 1:
        return True
    else:
        counter = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' or board[i][j] == 'X':
                    counter += 1
        if counter == 9:
            return None
        else:
            return False


def enter_move_player2(board):
    # The function draws the computer's move and updates the board.
    
    # Populate list with moves available as a normal list
    movesAvailable = movesAvailableCalc(board)
    
    # Get move from user
    userMove = int(input("Player 2 - Enter your move: "))
    while userMove not in movesAvailable:
        print("Space not available, try again")
        print("Available moves: ", movesAvailable)
        userMove = int(input("Player 2 - Enter your move: "))
        
    # Place user move into board array    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == userMove:
                board[i][j] = 'X'
                break
    
    # Place computer move on layout for output
    global layout
    for character in layout:
        if character == str(userMove):
            layout = layout.replace(character, "X")
    
    # Call to display board
    print("Player 2 move:")
    display_board(board)
    
    sign = "X"
    if victory_for(board, sign):
        print("Player 2 won!")
    elif victory_for(board, sign) == None:
        print("Game is tied")
    else:
        enter_move_player1(board)        

rows, cols = 3, 3
board = [[0 for i in range(rows)] for j in range(cols)]

counter = 1
for i in range(rows):
    for j in range(cols):
        board[i][j] = counter
        counter += 1

layout ="""
           |       |       
       1   |   2   |   3   
           |       |       
    -------+-------+-------
           |       |       
       4   |   5   |   6   
           |       |       
    -------+-------+-------
           |       |       
       7   |   8   |   9   
           |       |       
    """

print(layout)
print("""
    Player 1: O 
    Player 2: X
    """)
enter_move_player1(board)

    