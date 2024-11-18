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
