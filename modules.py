# Section 4: Modules
## Description:
# Introduce importing and using Python’s standard library.

## Key Concepts:
# - import keyword
# - Using functions from modules
# - Popular modules: math, random, os

## Code Demo:
import random
print("Random number:", random.randint(1, 10))

## Exercises:
# Use math module to compute square root.
import math

def square_root(num):
    if 1 <= num <= 10:
        return math.sqrt(num)
    else:
        return "invalid"

# num = random.randint(1,20)
# print("The randomly selected number is", num)
# print(square_root(num))


# Use random module to build a simple dice roller.
# The user should be prompted to roll the dice or quit the program
# This should be done in a continuous loop

# user_input = input("Input r to roll or q to quit: ")

# while user_input == "r":
#     num = random.randint(1,6)
#     print("The dice roll is", num)

#     if user_input == "q":
#         break
#     user_input = input("Enter r to roll or q to quit: ")

from datetime import datetime as dt

print(dt.now())

