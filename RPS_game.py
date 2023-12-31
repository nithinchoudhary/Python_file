import random
def get_user():
    while True:
        user_input = input("Enter 1 for rock, 2 for paper, 3 for scissor : ")
        if user_input == "q":
            exit()
        try:
            user_choice = int(user_input)
            if user_choice not in [1,2,3]:
                print("Invalid entry, please enter 1,2,3 or 'q'")
                continue
            return user_choice
        except ValueError:
            print("Invalid input, please enter a valid integer")
def get_winner(comp,user):
    if comp==user:
        return "MATCH IS TIE"
    elif (comp==1 and user==2)or(comp==2 and user==3)or(comp==3 and user==1):
        return "YOU WIN"
    else: return "YOU LOSE"
while True:
    comp=random.randint(1,3)
    user=get_user()
    winner=get_winner(comp,user)
    print(winner)