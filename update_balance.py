""" Written by Joseph Surrey, 21/04/2023
Edited 21/04/2023 to add functionality to remember how much the user spent at the start of the game
to tell them how much they won/raised for charity
Update balance function for Lucky Unicorn game
"""

# import information from other files
from print_balance import print_balance


def update_balance(balance, token, initial_payment):
    # add the amount the user won to their balance depending on the token
    balance += token[0][1]
    # print the users balance
    print_balance(balance, token, initial_payment)
