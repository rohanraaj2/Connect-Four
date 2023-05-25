import random


def game_status_decision():
    print("Start the game?")
    print("Y/N")
    starting_prompt = input()
    if starting_prompt == "Y":
        game_start_screen()
    elif starting_prompt == "N":
        start_screen()


def game_start_screen():
    print("Game started")
    print("Choose your opponent:")
    print("1. Human player")
    print("2. AI")
    player_choose = int(input())
    board_size = random.random(5)
    if player_choose.lower() == 1:
        human_vs_human(board_size)
    elif player_choose.capitalize() == 2:
        human_vs_AI(board_size)


def human_vs_human(board_size):
    while 
    player_1_turn()
    player_2_turn()
def player_1_turn(board_size):

    player_1_wins = False
    if (player_1_wins):
        return True
    print("Player 1's turn:")
    input("choose column: 1 to", board_size)
    player_1_column = int(input())


    print("R = restart")
    print("Q = quit")

    pass


def player_2_turn(board_size):
    print("Player 2's turn:")
    player_2_column = input("Select column")
    pass

def win_status(player):
    if player == "player_1":
        return 

def human_vs_AI(board_size):
    pass


def start_screen():
    print("Welcome to Connect Four")
    game_status_decision()


start_screen()
