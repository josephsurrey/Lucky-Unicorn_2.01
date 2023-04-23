""" Written by Joseph Surrey, 21/04/2023
Edited 21/04/2023 to add functionality to remember how much the user spent at the start of the game
to tell them how much they won/raised for charity
Updated 23/04/2023 to add constants for text formatting

Check for sufficient balance to continue function for Lucky Unicorn game
"""

# import information from other files
from setup import *
from quit import quit
from ask_user_if_they_would_like_to_continue import ask_user_if_they_would_like_to_continue


def check_for_sufficient_balance_to_continue(balance, initial_payment):
    if balance < ROUND_PRICE:
        # if user's balance is less than the price of a round, quit
        print("Insufficient funds to continue")
        # Section separator
        print(SECTION_SEPARATOR)
        quit(balance, initial_payment)
    else:
        # else ask the user if they would like to continue
        ask_user_if_they_would_like_to_continue(balance, initial_payment)
