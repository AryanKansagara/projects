'''
what i need:
->computer input
->choices for user
->user input
->win
->tie
->loose

'''

import random 

comp_turn = random.randint(1,3)

game_is_still_going = True




user = print("Press Enter to get started with the game")
def user_input():
    user = input("ROCK(r)||PAPER(p)||SCISSORS(s)") 
    user.lower()
    print(f"You selected {user}")

def flip():
    if comp_turn == 1:
        comp_turn = 'r'
    elif comp_turn == 2:
        comp_turn = 'p'
    elif comp_turn == 3:
        comp_turn = 's'
    

def game_win():
    global game_is_still_going
    if comp_turn == 'r' and user == 's':   
        game_is_still_going = False
        print("you LOOSE") 

    elif comp_turn == 'r' and user == 'p':
        game_is_still_going = False
        print("you WIN")

    elif comp_turn == user:
        game_is_still_going = False
        print("TIE")

    elif comp_turn == 'p' and user == 'r':
        game_is_still_going = False
        print("you LOOSE")

    elif comp_turn == 'p' and user == 's':
        game_is_still_going = False
        print("you WIN")

    elif comp_turn == 's' and user == 'p':
        game_is_still_going = False
        print("you LOOSE")

    elif comp_turn == 's' and user == 'r':
        game_is_still_going = False
        print("you WIN")


def play_game():
    while game_is_still_going:

        user_input()

        flip()

        game_win()

play_game()