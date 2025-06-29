####################################################
# Functions                                        #
####################################################

## Key Concepts:
# - def keyword
# - Parameters and arguments
# - Return values
# - Default arguments

## Code Demo:
# def greet(name="world"):
#     return f"Hello, {name}!"
# print(greet("Alice"))
# print(greet())

## Exercises:
# Write a function that returns the square of a number.

# Write a function that returns True if a number is even, False otherwise.

# Write a function that takes in someone's first and last name as 
# separate inputs and returns a string with the names combined

# Write a function that returns the minimum, maximum and the average of a list of numbers

####################################################
# Scope                                            #
####################################################

## Key Concepts:
# - Local vs global variables
# - Variable shadowing
# - Scope lifetime

## Code Demo:
# x = 10
# def change_x():
#     x = 5
#     print("Inside:", x)
# change_x()
# print("Outside:", x)

## Exercises:
# Predict output for different scope examples.

####################################################
# Debugging                                        #
####################################################

## Key Concepts:
# - Common errors (NameError, TypeError)
# - try/except blocks
# - print-debugging

## Code Demo:
# try:
#     val = int(input("Enter number: "))
#     print("Value is:", val)
# except ValueError:
#     print("Invalid input!")

## Exercises:
# Fix broken code snippets with bugs.

## Tips for Teaching:
# Encourage students to debug before asking for help.

####################################################
# Modules                                          #
####################################################

## Key Concepts:
# - import keyword
# - Using functions from modules
# - Popular modules: math, random, os

## Code Demo:
# import random
# print(random.randint(1, 10))

## Exercises:
# Use math module to compute square root.
# Use random module to build a simple dice roller.

# Pair Programming Project:
## Task:
# Build a number guessing game using:
# - Functions for game logic
# - random module
# - input/output
# - try/except for error handling
