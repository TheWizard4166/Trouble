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

import numpy as np
import random
from colorama import Fore, Back, Style

class player:
    def __init__(self, color):
        self.color = color
        self.score = 0
        

dice = random.randint(1,6)
print(dice)
