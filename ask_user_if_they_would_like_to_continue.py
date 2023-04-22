""" Written by Joseph Surrey, 21/04/2023
Edited 21/04/2023 to add functionality to remember how much the user spent at the start of the game
to tell them how much they won/raised for charity
Ask user if they would like to continue function for Lucky Unicorn game
"""

# import information from other files
from get_valid_input import get_valid_input
import start_round
from quit import quit


def ask_user_if_they_would_like_to_continue(balance, initial_payment):
    # ask the user if they would like to continue
    continue_ = get_valid_input("Would you like to play another round? ", str, ["Y", "YES", "N", "NO"], True)
    if continue_ == "Y" or continue_ == "YES":
        # if user enters "Y" or "YES" then start a new round
        from start_round import start_round
        start_round(balance, initial_payment)
    elif continue_ == "N" or continue_ == "NO":
        # else if user enters "N" or "NO" then quit
        quit(balance, initial_payment)
