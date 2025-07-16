####################################################
# Classes                                          #
####################################################

## Key Concepts:
# - class and __init__
# - self keyword
# - instance variables and methods

"""
BASIC STRUCTURE:

class <class name>:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def method1(self):
        pass

"""

class My_House():
    description = "Something you live in"

    def explode(self):
        print("Boom!")

house = My_House()
print(house.description)
house.explode()

ls = [1,2,3]
print(ls)


# Code Demo:
class Dog:

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

    def rename(self, name):
        self.name = name


# my_dog = Dog("Spot")
# print(my_dog.bark())


# TODO: Create a student class




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
