""" Written by Joseph Surrey, 4/04/2023
Edited 21/04/2023 to add functionality to remember how much the user spent at the start of the game
to tell them how much they won/raised for charity
Edited 21/04/2023 so that user presses enter to start after the initial payment is made
and not every round
Start round function for Lucky Unicorn game
"""

# import information from other files
from setup import *
from get_valid_input import get_valid_input
from generate_token import generate_token


def start_round(balance, inital_payment):
    # subtract the price of the round from the user's balance
    balance -= ROUND_PRICE
    # generate token
    generate_token(balance, inital_payment)
