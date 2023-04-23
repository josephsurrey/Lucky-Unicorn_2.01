"""
Written by Joseph Surrey 4/04/2023
Updated 21/04/2023 changed format of weights to work with random.choices()
Updated 21/04/2023 to add the instructions for the game
Updated 23/04/2023 to add constants for text formatting

Constants to be used in project
"""

# How much the user wins from each token
TOKEN_VALUE = [["unicorn", 5.0], ["zebra", 0.5], ["horse", 0.5], ["donkey", 0]]
# Chance of each token being generated
TOKEN_WEIGHT = [0.1, 0.3, 0.3, 0.3]
# Maximum spend per game
MAX_SPEND = 10
# How much each round costs
ROUND_PRICE = 1
# Instructions
INSTRUCTIONS = open('instructions.txt', 'r')

# Constants for text formatting
# Title
TITLE = "𝕃𝕦𝕔𝕜𝕪 𝕌𝕟𝕚𝕔𝕠𝕣𝕟"
# Separates different sections of the game
SECTION_SEPARATOR = "=" * 50
# Prefix for titles
TITLE_PREFIX = "\n\n=== "
# Suffix for titles
TITLE_SUFFIX = " ===\n"
# Prefix for messages
