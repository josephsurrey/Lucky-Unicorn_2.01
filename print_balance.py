""" Written by Joseph Surrey, 21/04/2023
Edited 21/04/2023 to add functionality to remember how much the user spent at the start of the game
to tell them how much they won/raised for charity
Updated 23/04/2023 to add constants for text formatting

Print balance function for Lucky Unicorn game
"""

# import information from other files
from check_for_sufficient_balance_to_continue import check_for_sufficient_balance_to_continue
from setup import *


def print_balance(balance, token, initial_payment):
    # print the token that the user got
    print(f"You found a {token[0][0]}")
    if token[0][0] != "donkey":
        # if the token is not a donkey, print how much the user won (rounded to 2 decimal places)
        print(f"You won ${token[0][1]:.2f}!")
    else:
        # if the token is a donkey, tell the user they didn't win anything
        print("You didn't win anything this round. Try again!")
    # print the users remaining balance (rounded to 2 decimal places)
    print(f"You have ${balance:.2f} left")
    # Section separator
    print(SECTION_SEPARATOR)
    # check for sufficient balance to continue
    check_for_sufficient_balance_to_continue(balance, initial_payment)

