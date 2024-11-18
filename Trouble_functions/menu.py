def main_menu():
    user_input = ""
    options = [1,2,3]
    while user_input not in options:
        print("######  MAIN MENU  ######")
        print("###### 1. Start    ######")
        print("###### 2. Options  ######")
        print("###### 3. Quit     ######")
        user_input = input("")
        try:
            user_input = int(user_input)
        except ValueError:
            print("Input a number!")
    return user_input

    
