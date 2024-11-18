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
current_turn = "yellow"

#initialize starting game board
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

                # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
trouble_board = ([y1,s, y, s, y, s, y, s, o, s, b, s, b, s, b, s, b1],
                 [y2,y, s, s, s, s, s, s, s, s, s, s, s, s, s, b, b2],
                 [y3,s, s, y, s, s, s, s, s, s, s, s, s, b, s, s, b3],
                 [y4,y, s, s, y, s, s, s, s, s, s, s, b, s, s, b, b4],
                 [s, s, s, s, s, y, s, s, s, s, s, b, s, s, s, s, s],
                 [s, y, s, s, s, s, y, s, s, s, b, s, s, s, s, b, s],
                 [s, s, s, s, s, s, u, d, d, d, u, s, s, s, s, s, s],
                 [s, o, s, s, s, s, u, s, s, s, u, s, s, s, s, o, s],
                 [s, s, s, s, s, s, u, d, d, d, u, s, s, s, s, s, s],
                 [s, g, s, s, s, s, g, s, s, s, r, s, s, s, s, r, s],
                 [s, s, s, s, s, g, s, s, s, s, s, r, s, s, s, s, s],
                 [g1,g, s, s, g, s, s, s, s, s, s, s, r, s, s, r, r1],
                 [g2,s, s, g, s, s, s, s, s ,s ,s, s, s, r, s, s, r2],
                 [g3,g, s, s, s, s, s, s, s, s, s, s, s, s, s, r, r3],
                 [g4,s, g, s, g, s, g, s, o, s, r, s, r, s, r, s, r4])

dice = random.randint(1,6)
print(dice)
