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
