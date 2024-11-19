import settings
def add_pawn(turn):
    '''Adds a new pawn onto the board, takes in color of the player as argument'''

    if turn == "yellow":
        if trouble_board[0][2] == y: #if open space to move pawn to 
            for i in range(4): 
                if trouble_board[i][0] != s:
                    trouble_board[0][2] = trouble_board[i][0]
                    trouble_board[i][0] = s
                    break
    elif turn == "blue":
        if trouble_board[1][15] == b: #if open space to move pawn to 
            for i in range(4): 
                if trouble_board[i][16] != s:
                    trouble_board[1][15] = trouble_board[i][16]
                    trouble_board[i][16] = s
                    break
    elif turn == "green":
        if trouble_board[13][1] == g: #if open space to move pawn to 
            for i in range(11,15): 
                if trouble_board[i][0] != s:
                    trouble_board[13][1] = trouble_board[i][0]
                    trouble_board[i][0] = s
                    break
        if trouble_board[14][14] == r: #if open space to move pawn to 
            for i in range(11,15): 
                if trouble_board[i][16] != s:
                    trouble_board[14][14] = trouble_board[i][16]
                    trouble_board[i][16] = s
                    break

def pawns_off_board(turn):
    '''Returns a bool that shows whether a player has any pawns not on the board yet'''
    if turn == "yellow":
        for i in range(4): #check if any pawns are off the board
            if trouble_board[i][0] != s:
                return(True)
        return(False)
    if turn == "blue":
        for i in range(4): #check if any pawns are off the board
            if trouble_board[i][16] != s:
                return(True)
        return(False)
    if turn == "green":
        for i in range(11,15): #check if any pawns are off the board
            if trouble_board[i][0] != s:
                return(True)
        return(False)
    if turn == "red":
        for i in range(11,15): #check if any pawns are off the board
            if trouble_board[i][16] != s:
                return(True)
        return(False)

def move_pawn(spaces):
    '''Moves a selected colored pawn the given number of spaces'''
    pawn_to_move = input("Which pawn on the board would you like to move(1/2/3/4)?: ")
    print(current_turn[0]+pawn_to_move)
