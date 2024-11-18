# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Emily Lou
#               James Bryant
#               Jessica Reichert
#               Wallace Wang
# Section:      521            
# Assignment:           
# Date:         15 November 2024

"""
   Each player will have their own class to assign the variable 
"""


import numpy as np
import random
import colorama 
import Trouble_functions

#global variables
#pawn counts on and off the board
y_pawns_off, b_pawns_off, g_pawns_off, r_pawns_off = 4
y_pawns_on, b_pawns_on, g_pawns_on, r_pawns_on = 0

#initialize starting game board
s = "   "
y = " "+colorama.Fore.YELLOW +"o"+colorama.Style.RESET_ALL+" "
b = " "+colorama.Fore.BLUE +"o"+colorama.Style.RESET_ALL+" "
g = " "+colorama.Fore.GREEN +"o"+colorama.Style.RESET_ALL+" "
r = " "+colorama.Fore.RED +"o"+colorama.Style.RESET_ALL+" "
o = " o "
d = "---"
u = " | "
                # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
trouble_board = ([s, y, s, y, s, y, s, o, s, b, s, b, s, b, s],
                 [y, s, s, s, s, s, s, s, s, s, s, s, s, s, b],
                 [s, s, y, s, s, s, s, s, s, s, s, s, b, s, s],
                 [y, s, s, y, s, s, s, s, s, s, s, b, s, s, b],
                 [s, s, s, s, y, s, s, s, s, s, b, s, s, s, s],
                 [y, s, s, s, s, y, s, s, s, b, s, s, s, s, b],
                 [s, s, s, s, s, u, d, d, d, u, s, s, s, s, s],
                 [o, s, s, s, s, u, s, s, s, u, s, s, s, s, o],
                 [s, s, s, s, s, u, d, d, d, u, s, s, s, s, s],
                 [g, s, s, s, s, g, s, s, s, r, s, s, s, s, r],
                 [s, s, s, s, g, s, s, s, s, s, r, s, s, s, s],
                 [g, s, s, g, s, s, s, s, s, s, s, r, s, s, r],
                 [s, s, g, s, s, s, s, s ,s ,s, s, s, r, s, s],
                 [g, s, s, s, s, s, s, s, s, s, s, s, s, s, r],
                 [s, g, s, g, s, g, s, o, s, r, s, r, s, r, s])

dice = random.randint(1,6)
print(dice)
