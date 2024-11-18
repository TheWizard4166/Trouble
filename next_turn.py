def next_turn():
    global current_turn
    turns_dict = {"yellow":1, 1:"yellow", "blue":2, 2:"blue", "green":3, 3:"green", "red":4, 4:"red"}
    if turns_dict[current_turn]+1 >=5:
        current_turn = (turns_dict[turns_dict[current_turn]-3])
    else:
        current_turn = (turns_dict[turns_dict[current_turn]+1])
