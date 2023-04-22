""" Written by Joseph Surrey, 21/04/2023
Print balance function for Lucky Unicorn game
"""

# import information from other files
from check_for_sufficient_balance_to_continue import check_for_sufficient_balance_to_continue


def print_balance(balance, token):
    # print the token that the user got
    print(f"You found a {token[0][0]}")
    if token[0] != "donkey":
        # if the token is not a donkey, print how much the user won, rounded to 2 decimal places
        print(f"You won ${round(token[0],1), 2}!")
    else:
        # if the token is a donkey, tell the user they didn't win anything
        print("You didn't win anything this round. Try again!")
    # print the users remaining balance
    print(f"You have ${round(balance, 2)} left")
    # check for sufficient balance to continue
    check_for_sufficient_balance_to_continue(balance)

