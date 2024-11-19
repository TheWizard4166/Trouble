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
from Trouble_functions import settings, display  
import sys

# adding Trouble_functions to the system path
#sys.path.insert(0, 'Trouble_functions/')
settings.init()
dice = random.randint(1,6)
print(dice)
display.print_board()
#help(display)
