def print_board(trouble_board):
    '''Prints out the current board to the console'''
    for row in trouble_board:
        for space in row:
            print(space,end="")
        print("\n",end="")

