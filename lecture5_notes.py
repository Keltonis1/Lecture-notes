####################################################
# Classes                                          #
####################################################

## Key Concepts:
# - class and __init__
# - self keyword
# - instance variables and methods

## Code Demo:
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def bark(self):
#         return f"{self.name} says woof!"
# d = Dog("Buddy")
# print(d.bark())

## Exercises:
# Create a class for a `BankAccount` with `deposit()` and `withdraw()` methods.

# Add a print account summary method (use __str__)

####################################################
# Inheritance                                      #
####################################################

## Key Concepts:
# - Inheriting with `class SubClass(ParentClass):`
# - Overriding methods
# - super()

## Code Demo:
# class Animal:
#     def speak(self):
#         return "Some sound"
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
# print(Dog().speak())

## Exercises:
# Create a `Vehicle` class and extend it into `Car` and `Bike`.
# Create a `Shape` class and inherit `Rectangle` and `Circle` with methods to compute area.

####################################################
# File I/O                                         #
####################################################

## Key Concepts:
# - open(), read(), write(), close()
# - Using `with open()` for context management

## Code Demo:
# with open("data.txt", "w") as f:
#     f.write("Hello, file!")

# with open("data.txt", "r") as f:
#     print(f.read())

## Exercises:
# Write a program that appends user input to a file.

# Pair Programming Project:
## Task:
# Refactor the guessing game into a class (`GuessingGame`)
# - Use inheritance if possible (e.g., Game → GuessingGame)
# - Log game rounds to a file

## Time:
# 40–50 minutes
