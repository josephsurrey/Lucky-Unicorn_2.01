""" Written by Joseph Surrey, 4/04/2023
Edited 21/04/2023 to add functionality to remember how much the user spent at the start of the game
to tell them how much they won/raised for charity
Edited 21/04/2023 so that user presses enter to start after the initial payment is made
and not every round
Initial payment function for Lucky Unicorn game
"""

# import information from other files
from get_valid_input import get_valid_input
from start_round import start_round
from setup import *


def initial_payment():
    # set balance to number user has entered
    balance = get_valid_input(f"How much would you like to play Lucky Unicorn with? (${ROUND_PRICE} - ${MAX_SPEND}) ",
                              float, [], False, ROUND_PRICE, MAX_SPEND)
    initial_payment = balance
    # prompt user to press enter to start
    get_valid_input("Press enter to start: ", str, [""])
    # start the round
    start_round(balance, initial_payment)
