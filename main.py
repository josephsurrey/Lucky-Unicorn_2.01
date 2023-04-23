""" Written by Joseph Surrey, 21/04/2023
Main loop for Lucky Unicorn game
"""

# import components
from instructions import instructions
from setup import *


# main loop
def main():
    print(TITLE_PREFIX, TITLE, TITLE_SUFFIX)
    instructions()


main()
