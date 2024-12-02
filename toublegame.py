# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jessica Reichert
#               James Bryant
#               Emily Lou
#               Wallace Wang
# Section:      521
# Assignment:   Lab 13 
# Date:         17 November 2024
#

import colorama
import random
#import numpy as np
#import sys

def next_turn():
    global current_turn
    turns_dict = {"yellow":1, 1:"yellow", "blue":2, 2:"blue", "red":3, 3:"red", "green":4, 4:"green"}
    if turns_dict[current_turn]+1 >=5:
        current_turn = (turns_dict[turns_dict[current_turn]-3])
    else:
        current_turn = (turns_dict[turns_dict[current_turn]+1])

def dice_roll():
    print(f'It is {current_turn}\'s turn!')
    print_board()
    roll = random.randint(1,6)
    with open("Rolls.txt", 'a') as file:
        file.write(str(roll))
    print(f'{current_turn} rolled: {roll}')
    while roll == 6:
        new_pawn = input("Enter a new pawn?(Y/N): ")
        if new_pawn == "Y": 
            add_pawn(current_turn)
        else:
            move_pawn(6)
        print_board()
        roll = random.randint(1,6)
        print(f'next roll: {roll}')
    if pawns_on_board(current_turn) >= 1:
        move_pawn(roll)
    print_board()
    next_turn()

def pawns_on_board(turn):
    '''Returns a int of the number of pawns on the board'''
    pawn_count = 0
    if turn == "yellow":
        for i in range(4): #check if any pawns are off the board
            if trouble_board[i][0] == s:
                pawn_count+=1
        #return(pawn_count)
    if turn == "blue":
        for i in range(4): #check if any pawns are off the board
            if trouble_board[i][16] == s:
                pawn_count+=1
        #return(pawn_count)
    if turn == "green":
        for i in range(11,15): #check if any pawns are off the board
            if trouble_board[i][0] == s:
                pawn_count+=1
        #return(pawn_count)
    if turn == "red":
        for i in range(11,15): #check if any pawns are off the board
            if trouble_board[i][16] == s:
                pawn_count+=1
        #return(pawn_count)
    #print(pawn_count)
    return(pawn_count)

def send_home(pawn):
    variable_dict = {y1:"y1", y2:"y2", y3:"y3", y4:"y4", b1:"b1", b2:"b2", b3:"b3", b4:"b4", r1:"r1", r2:"r2", r3:"r3", r4:"r4", g1:"g1", g2:"g2", g3:"g3", g4:"g4"}
    name = variable_dict[pawn]
    if name[0] == "y":
        trouble_board[int(name[1])-1][0] = pawn
    elif name[0] == "b":
        trouble_board[int(name[1])-1][16] = pawn
    elif name[0] == "r":
        trouble_board[int(name[1])+10][16] = pawn
    else: #== "g"
        trouble_board[int(name[1])+10][0] = pawn

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
    
def add_pawn(turn):
    '''Adds a new pawn onto the board, takes in color of the player as argument'''

    if turn == "yellow":
        if trouble_board[0][2] != y1 or y2 or y3 or y4: #if open space to move pawn to 
            #if trouble_board[0][2] != y: #if there is another player on the space, send home
                #send_home(trouble_board[0][2])

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
    else:
        if trouble_board[14][14] == r: #if open space to move pawn to 
            for i in range(11,15): 
                if trouble_board[i][16] != s:
                    trouble_board[14][14] = trouble_board[i][16]
                    trouble_board[i][16] = s
                    break

def find_index(array, pawn_look_for):
    variable_dict = {"y1":y1, "y2":y2, "y3":y3, "y4":y4, "b1":b1, "b2":b2, "b3":b3, "b4":b4, "r1":r1, "r2":r2, "r3":r3, "r4":r4, "g1":g1, "g2":g2, "g3":g3, "g4":g4}
    pawn_look_for = variable_dict[pawn_look_for]
    for row_index, row in enumerate(array):
        if pawn_look_for in row:
            col_index = row.index(pawn_look_for)
            return row_index, col_index


def move_pawn(spaces):
    '''Moves a selected colored pawn the given number of spaces'''
    pawn_to_move = input("Which pawn on the board would you like to move(1/2/3/4)?: ")
    pawn = (current_turn[0]+pawn_to_move)
    row = find_index(trouble_board, pawn)[0] 
    col = find_index(trouble_board, pawn)[1]
    #TOP ROW
    if row == 0: 
        for i in range(spaces):
            if col == 14: #unless its in corner spot
                newrow = row+1
                newcol = col+1
                #if space not blank send player home
            else:
                if i == 0:
                    newcol = col+2
                    newrow = row
                else:
                    if newcol == 14:
                        newrow+=1
                        newcol+=1
                    elif newcol == 15:
                        newrow+=2
                    else:
                        newcol+=2
                #if space not blank send player home
        empty_vars = [y,b,r,g,o]
        if trouble_board[newrow][newcol] not in empty_vars:
            send_home(trouble_board[newrow][newcol])
        trouble_board[newrow][newcol] = trouble_board[row][col]
        #if prev space was yellow turn open yellow if blue turn open blue
        if col < 8:
            trouble_board[row][col] = y
        elif col > 8:
            trouble_board[row][col] = b
        else:
            trouble_board[row][col] = o
    #BOT ROW
    elif row == 14: 
        for i in range(spaces):
            if col == 2: #unless its in corner spot
                newrow = row-1
                newcol = col-1
                #if space not blank send player home
            else:
                if i == 0:
                    newcol = col-2
                    newrow = row
                else:
                    if newcol == 2:
                        newrow-=1
                        newcol-=1
                    elif newcol == 1:
                        newrow-=2
                    else:
                        newcol-=2                    
                #if space not blank send player home
        empty_vars = [y,b,r,g,o]
        if trouble_board[newrow][newcol] not in empty_vars:
            send_home(trouble_board[newrow][newcol])
        trouble_board[newrow][newcol] = trouble_board[row][col]
        #if prev space was green turn open green, if red turn open red
        if col < 8:
            trouble_board[row][col] = g
        elif col > 8:
            trouble_board[row][col] = r
        else:
            trouble_board[row][col] = o
    #LEFT COL
    elif col == 1:
        for i in range(spaces):
            if row == 1: #unless its in corner spot
                newrow = row-1
                newcol = col+1
                #if space not blank send player home
            else:
                if i == 0:
                    newrow = row-2
                    newcol = col
                else: 
                    if newrow == 1:
                        newrow-=1
                        newcol+=1
                    elif newrow == 0:
                        newcol+=2
                    else:
                        newrow-=2   
                #if space not blank send player home
        trouble_board[newrow][newcol] = trouble_board[row][col]
        #if prev space was yellow turn open yellow, if green turn open green
        if row < 7:
            trouble_board[row][col] = y
        elif row > 7:
            trouble_board[row][col] = g
        else:
            trouble_board[row][col] = o
    #RIGHT COL
    elif col == 15: 
        for i in range(spaces):
            if row == 13: #unless its in corner spot
                newrow = row+1
                newcol = col-1
                #if space not blank send player home
            else:
                if i ==0:
                    newrow = row+2
                    newcol= col
                else:
                    if newrow == 13:
                        newrow+=1
                        newcol-=1
                    elif newrow == 14:
                        newcol -=2
                    else:
                        newrow+=2
                #if space not blank send player home
        trouble_board[newrow][newcol] = trouble_board[row][col]
        #if prev space was blue turn open blue, if red turn open red
        if row < 7:
            trouble_board[row][col] = b
        elif row > 7:
            trouble_board[row][col] = r
        else:
            trouble_board[row][col] = o

def print_board():
    '''Prints out the current board to the console'''
    for row in trouble_board:
        for space in row:
            print(space,end="")
        print("\n",end="")

#def send_pawn_home(space):


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
    print("######      MAIN MENU        ######")
    print("######      1. Start         ######")
    print("######      2. Instructions  ######")
    print("######      3. Quit          ######")
    user_input = input("")
    try:
        user_input = int(user_input)
    except ValueError:
        print("Input a number!")
        return main_menu()
    if user_input > 3:
        print("Input one of the options!")
        return main_menu()
    elif user_input == 3:
        return 
    elif user_input == 2:
        print_instructions()
    elif user_input == 1:
        return start()


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
    print()

#MAINNNNNNNNNNNNNNNNNNNNNN
#testing


#initialize starting game board
s = "   "
y = " "+colorama.Fore.YELLOW +"o"+colorama.Style.RESET_ALL+" "
b = " "+colorama.Fore.BLUE +"o"+colorama.Style.RESET_ALL+" "
g = " "+colorama.Fore.GREEN +"o"+colorama.Style.RESET_ALL+" "
r = " "+colorama.Fore.RED +"o"+colorama.Style.RESET_ALL+" "
o = " o "
d = "---"
u = " | "
y1 = " "+colorama.Fore.YELLOW +"●"+colorama.Style.RESET_ALL+"1"
b1 = " "+colorama.Fore.BLUE +"●"+colorama.Style.RESET_ALL+"1"
g1 = " "+colorama.Fore.GREEN +"●"+colorama.Style.RESET_ALL+"1"
r1 = " "+colorama.Fore.RED +"●"+colorama.Style.RESET_ALL+"1"
y2 = " "+colorama.Fore.YELLOW +"●"+colorama.Style.RESET_ALL+"2"
b2 = " "+colorama.Fore.BLUE +"●"+colorama.Style.RESET_ALL+"2"
g2 = " "+colorama.Fore.GREEN +"●"+colorama.Style.RESET_ALL+"2"
r2 = " "+colorama.Fore.RED +"●"+colorama.Style.RESET_ALL+"2"
y3 = " "+colorama.Fore.YELLOW +"●"+colorama.Style.RESET_ALL+"3"
b3 = " "+colorama.Fore.BLUE +"●"+colorama.Style.RESET_ALL+"3"
g3 = " "+colorama.Fore.GREEN +"●"+colorama.Style.RESET_ALL+"3"
r3 = " "+colorama.Fore.RED +"●"+colorama.Style.RESET_ALL+"3"
y4 = " "+colorama.Fore.YELLOW +"●"+colorama.Style.RESET_ALL+"4"
b4 = " "+colorama.Fore.BLUE +"●"+colorama.Style.RESET_ALL+"4"
g4 = " "+colorama.Fore.GREEN +"●"+colorama.Style.RESET_ALL+"4"
r4 = " "+colorama.Fore.RED +"●"+colorama.Style.RESET_ALL+"4"

                # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14  15 16
trouble_board = ([y1,s, y, s, y, s, y, s, o, s, b, s, b, s, b, s, b1], #0
                 [y2,y, s, s, s, s, s, s, s, s, s, s, s, s, s, b, b2], #1
                 [y3,s, s, y, s, s, s, s, s, s, s, s, s, b, s, s, b3], #2
                 [y4,y, s, s, y, s, s, s, s, s, s, s, b, s, s, b, b4], #3
                 [s, s, s, s, s, y, s, s, s, s, s, b, s, s, s, s, s], #4
                 [s, y, s, s, s, s, y, s, s, s, b, s, s, s, s, b, s], #5
                 [s, s, s, s, s, s, u, d, d, d, u, s, s, s, s, s, s], #6
                 [s, o, s, s, s, s, u, s, s, s, u, s, s, s, s, o, s], #7
                 [s, s, s, s, s, s, u, d, d, d, u, s, s, s, s, s, s], #8
                 [s, g, s, s, s, s, g, s, s, s, r, s, s, s, s, r, s], #9
                 [s, s, s, s, s, g, s, s, s, s, s, r, s, s, s, s, s], #10
                 [g1,g, s, s, g, s, s, s, s, s, s, s, r, s, s, r, r1], #11
                 [g2,s, s, g, s, s, s, s, s ,s ,s, s, s, r, s, s, r2], #12
                 [g3,g, s, s, s, s, s, s, s, s, s, s, s, s, s, r, r3], #13
                 [g4,s, g, s, g, s, g, s, o, s, r, s, r, s, r, s, r4]) #14

global current_turn
#starting turn
def start():
    global current_turn
    print_instructions()
    #main_menu()
    current_turn = "yellow"

    while True:
        dice_roll()
    #add_pawn(current_turn)
    #print(current_turn)
    ##add_pawn(current_turn)

    #print(current_turn)
    #add_pawn(current_turn)
    #print_board()



main_menu()
