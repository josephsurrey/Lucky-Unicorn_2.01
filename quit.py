""" Written by Joseph Surrey, 21/04/2023
Updated 23/04/2023 to add constants for text formatting

Quit function for Lucky Unicorn game
"""
from setup import SECTION_SEPARATOR


def quit(balance, initial_payment):
    # Thank user for playing
    print("Thanks for playing Lucky Unicorn")
    # Print the remaining balance of the user (rounded to 2 decimal places)
    print(f"Remaining balance: ${balance:.2f}")
    if balance >= initial_payment:
        # If the user has more or equal money to what they started with print how much they won
        # (rounded to 2 decimal places)
        print(f"You won ${balance - initial_payment:.2f}")
        # Section break
        print(SECTION_SEPARATOR)
    else:
        # Print how much the user raised for charity (rounded to 2 decimal places)
        print(f"You raised ${initial_payment - balance:.2f} for charity")
        # Section break
        print(SECTION_SEPARATOR)
