#import settings
def next_turn():
    global current_turn
    turns_dict = {"yellow":1, 1:"yellow", "blue":2, 2:"blue", "red":3, 3:"red", "green":4, 4:"green"}
    if turns_dict[current_turn]+1 >=5:
        current_turn = (turns_dict[turns_dict[current_turn]-3])
    else:
        current_turn = (turns_dict[turns_dict[current_turn]+1])
