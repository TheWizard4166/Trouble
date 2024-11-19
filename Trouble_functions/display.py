import settings
'''
    The display file for Trouble.
'''

def print_board():
    '''Prints out the current board to the console'''
    for row in trouble_board:
        for space in row:
            print(space,end="")
        print("\n",end="")

def main_menu():
    '''
        Prints out the main menu and asks for apropriate responses.
        If the user inputs:
            1: Starts Game
            2: Displays option menu
            3: Quits game
    '''
    user_input = ""
    options = [1,2,3]
    while user_input not in options:
        print("######  MAIN MENU  ######")
        print("###### 1. Start    ######")
        print("###### 2. Options  ######")
        print("###### 3. Quit     ######")
        user_input = input("")
        try:
            user_input = int(user_input)
        except ValueError:
            print("Input a number!")
    return user_input

def print_instructions():
    print("Game Rules\n")
    
    print("Rolling a Six:")
    print("  - To move a peg from 'Home' to the 'Start' space, you must roll a six.")
    print("  - If you roll a six, you get an additional roll.")
    print("  - You can move a peg out of 'Home' or move one of your pegs already in play.\n")
    
    print("Moving Around the Board:")
    print("  - On your turn, move one of your pegs forward the number of spaces indicated by the die.")
    print("  - Pegs move in a clockwise direction around the board.\n")
    
    print("Bumping:")
    print("  - If your peg lands on a space occupied by another player's peg, that peg is bumped back to its 'Home' area.")
    print("  - The player must roll a six to move it back onto the board.\n")
    
    print("Getting to the Finish:")
    print("  - Once a peg has completed the circuit around the board, it moves into the 'Finish' area.")
    print("  - An exact roll is required to move a peg into the Finish.\n")
    
    print("Winning the Game:")
    print("  - The first player to move all four of their pegs into the Finish area wins the game.")
    

