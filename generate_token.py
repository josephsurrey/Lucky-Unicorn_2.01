""" Written by Joseph Surrey, 21/04/2023
Edited 21/04/2023 to add functionality to remember how much the user spent at the start of the game
to tell them how much they won/raised for charity
Generate token function for Lucky Unicorn game
"""

# Import necessary libraries
import random
# Import information from other files
from setup import *
from update_balance import update_balance


def generate_token(balance, initial_payment):
    # generate a random token, using weights defined in setup to work out the chances of each token appearing
    token = random.choices(TOKEN_VALUE, weights=TOKEN_WEIGHT)
    # update the users balance
    update_balance(balance, token, initial_payment)
