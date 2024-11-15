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
from colorama import Fore, Back, Style

class player:
    def __init__(self, color, is_turn=False):
        self.color = color
        self.score = 0
        self.pawns_on_board = 0 
        self.pawns_held = 4
        self.is_turn = is_turn
    
    def add_pawn_to_board(self):
        pass
    def toggle_turn(self):
        self.is_turn = not self.is_turn

dice = random.randint(1,6)
print(dice)
