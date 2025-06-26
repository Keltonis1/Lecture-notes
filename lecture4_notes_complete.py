
# Lecture 4: Functions, Scope, Modules, Debugging
# Time: 3 hours
# Structure: 60% Slides + Code Demos, 40% Pair Programming

# Section 1: Functions
## Description:
# Introduce the concept of functions as reusable blocks of code.

## Key Concepts:
# - def keyword
# - Parameters and arguments
# - Return values
# - Default arguments

## Code Demo:
def greet(name="world"):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet())

## Exercises:
# 1. Write a function that returns the square of a number.
def square(x):
    return x * x

print(square(4))
# 2. Write a function that returns True if a number is even, False otherwise.
def is_even(n):
    return n % 2 == 0

print(is_even(3), is_even(4))

## Tips for Teaching:
# Emphasize function reuse and testing with different inputs.

# Section 2: Scope
## Description:
# Explain how variable visibility changes inside and outside functions.

## Key Concepts:
# - Local vs global variables
# - Variable shadowing
# - Scope lifetime

## Code Demo:
x = 10
def change_x():
    x = 5
    print("Inside:", x)

change_x()
print("Outside:", x)

## Exercises:
# Predict output for different scope examples.
# Create a function that modifies a global variable using the global keyword.
counter = 0

def increment():
    global counter
    counter += 1

increment()
print("Counter:", counter)

## Tips for Teaching:
# Use diagrams to show local/global memory locations.

# Section 3: Debugging
## Description:
# Teach students how to read error messages and use try/except.

## Key Concepts:
# - Common errors (NameError, TypeError)
# - try/except blocks
# - print-debugging

## Code Demo:
try:
    val = int(input("Enter number: "))
    print("Value is:", val)
except ValueError:
    print("Invalid input!")

## Exercises:
# Fix broken code snippets with bugs.
# Write a function that divides two numbers and handles division by zero.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def abs(x):
    """ Assumes x is an int
    Returns x if x>=0 and –x otherwise """
    if x < -1:
        print(x)
        return -x
    else:
        print(x)
        return x

print(safe_divide(10, 0))

## Tips for Teaching:
# Encourage students to debug before asking for help.

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
print("Square root of 16:", math.sqrt(16))
# Use random module to build a simple dice roller.
def roll_dice():
    return random.randint(1, 6)

print("Dice roll:", roll_dice())

## Tips for Teaching:
# Reinforce module reuse for simplifying code.

# Pair Programming Project:
## Task:
# Build a number guessing game using:
# - Functions for game logic
# - random module
# - input/output
# - try/except for error handling
