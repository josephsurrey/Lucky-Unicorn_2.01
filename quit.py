""" Written by Joseph Surrey, 21/04/2023
Quit function for Lucky Unicorn game
"""


def quit(balance, initial_payment):
    # Thank user for playing
    print("Thanks for playing Lucky Unicorn")
    # Print the remaining balance of the user (rounded to 2 decimal places)
    print(f"Remaining balance: ${balance:.2f}")
    if balance >= initial_payment:
        # If the user has more or equal money to what they started with print how much they won
        # (rounded to 2 decimal places)
        print(f"You won ${balance - initial_payment:.2f}")
    else:
        # Print how much the user raised for charity (rounded to 2 decimal places)
        print(f"You raised ${initial_payment - balance:.2f} for charity")
