import random

def dice_roll():
    print(f'It is {current_turn}\'s turn!')
    print_board()
    roll = random.randint(1,6)
    print(f'rolled: {roll}')
    while roll == 6:
        new_pawn = input("Enter a new pawn?(Y/N): ")
        if new_pawn == "Y": 
            add_pawn(current_turn)
        print_board()
        else:
            move_pawn(6)
        roll = random.randint(1,6)
        print(f'next roll: {roll}')
  
    move_pawn(roll)
    print_board()
    next_turn()
