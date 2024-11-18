import random

def dice_roll():
    roll = random.randint(1,6)
    while roll == 6:
        new_pawn = input("Enter a new pawn?(Y/N): ")
        if new_pawn =+ "Y": 
            add_pawn(current_turn)
        else:
            move_pawn(6)
        roll = random.randint(1,6)
  
    move_pawn(roll)
