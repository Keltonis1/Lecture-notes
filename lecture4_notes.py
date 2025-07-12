

# number = 0
# while number < 10:
#     print(number)
#     number += 1


# print(5 % 3)

# x = 0
# while True:
#     if x % 2 == 0:
#         x += 1 # x becomes 1
#         continue

#     print(x)

#     # x += 1
#     if x > 10:
#         break


# x = 0
# while x <= 10:

#     print("I'm stuck")
#     x += 1



####################################################
# For Loops                                        #
####################################################

# my_list = [1,2,3,4,5,6]

# for number in my_list:
#     print(number)

# ind = 0
# while ind < len(my_list):
#     print(my_list[ind])

#     ind += 1



# TODO: Make a for loop that modifies this list to add five to each element in it.

# numbers = [1,2,3,4,5,6]  # [6,7,8,9,10,11]
# new_numbers = []

# for number in numbers:
#     new_numbers.append(number + 5)
#     # numbers.remove(number)
#     # print(numbers)
#     # number += 5
#     # list(number + 5)
#     # print(number)

# print(new_numbers)


# return the sum of all number in a list

# my_numbers = [3,4234,432,2,3,4,3,443,4234]
# sum = 0

# for number in my_numbers:
    # print(number)
    # sum = sum + number
    # sum += number
    # break continue
    # print(sum)


# print(sum)


#Lists can take up multiple lines if needed
my_list = [
    "Hello",0,23,67854,"world",57485,
    "Nice",56,-1,"to",-1,-78697495,"meet",
    "you",75847
]

#this loop prints out only strings
# for item in my_list:
#     if isinstance(item,int): #skip integers
#         continue
#     print(item)



# item = 5

# print(isinstance(56,str))

# print(type(56.43))
# print(isinstance(56.43,int))







# TODO: Make a for loop that prints the numbers 1 through 10
# string[0:5:2]

# range(0, 5, 1)
# [0,1,2,3,4]

# my_list = [
#     "Hello",0,23,67854,"world",57485,
#     "Nice",56,-1,"to",-1,-78697495,"meet",
#     "you",75847
# ]

# for i in range(0,len(my_list)):
#     print(i, my_list[i])



# for i in range(0,100):
#     if i % 2 == 1:
#         continue
#     if i >= 20:
#         break

    # print(i)




# TODO: Write this in a while loop format


# TODO: Use the provided for loop and the continue keyword, print every other number using
#       up until the number 20

# for i in range(100):


# TODO: Do the same thing just by calling range and using a different step



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


# def test_function():
#     print("Hello, World!")

# test_function()


# def another_function():
#     for i in range(10):
#         print(i)

# another_function()

# def say_hello(greeting):
#     print(greeting)

# say_hello("Hello!")

# def greet_many_times(greeting, number_times):
#     return 10


# number = greet_many_times("Hello!", 1000)

# print(number)

# len(list)


## Exercises:
# Write a function that returns the square of a number.

# def square(number):
#     return number * number

# print(square(5))

# def stop_at_five(count):
#     for num in range (count):
#         if num == 5:
#             return 5
#         else:
#             print(num)

        # print("Got to the end")

# num = stop_at_five(10)

# print(num)


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
