####################################################
# First print statement! Hello world               #
####################################################

# TODO: Write a statement that prints "Hello, world!"

# print("Hello, world!")


####################################################
# Introduction to variables                        #
####################################################

apples = 5
oranges = 6
fruits = apples + oranges

# TODO: In a cordial way, tell the user how many fruits we have

"""
# ANSWER:
print("Hello! You have", fruits, "fruits!")
"""

age = 20
name = "John"

# TODO: Print name and age in the format: "<name> is <age> years old!" POLL

"""
# ANSWER:
print(name, "is", age, "years old!")
"""

# examples of snake_case

"""
# ANSWER:
teachers_name = "kelson"
game_duration = 10 # minutes
weekend_plan = "beach"
my_weight = 180 # pounds
"""


####################################################
# Data types and Casting                           #
####################################################

# TODO: Find what each of these prints out. POLL

# print()
# print(type(5))
# print(type(3.45))
# print(type(-2.))
# print(type("what type is this?"))

# print(type(int("5")))
# print(type(int("5.3")))
# print(type(5 + 0.0))


my_age = "5.2"
his_age = "10.6"

# TODO: Cast these into integers and find the difference in their ages. BUGFIX

"""
# ANSWER:
print(int(my_age))
print(int(his_age))

print(float(my_age))
print(float(his_age))

print(int(float(my_age)))
print(int(float(his_age)))

difference = int(float(my_age)) - int(float(his_age))
"""


# TODO: Look through these examples of operations and make sure you know what they all do

# print(7 + 18)
# print(9. - 3)
# print(3 * 5)
# print(6 / 2)
# print(6 // 2)
# print(7.5 // 3)
# print(20 % 4)
# print(23 % 4)
# print(7.5 % 3)
# print(5 ** 4)
# print(2 * 3 + 1)
# print(2 * (3 + 1))


####################################################
# User Input                                       #
####################################################

# food_to_deliver = input("This is doordash. Please enter a food you would like")

# TODO: Uncomment the line above, then print a statement in the format: "Okay. Delivering your <food> now."

"""
# ANSWER:
print("Okay. Delivering your", food_to_deliver, "now.")
"""


# TODO: Write a program that takes a number and multiplies it by 5.

"""
# ANSWER:
number = int(input("Please enter a number"))
print("Your number multiplied by 5 is,", number * 5, "!")
"""

####################################################
# Pair Programming                                 #
####################################################


"""
PROBLEM 1:
Make a python program, that takes two user inputs, each for a number.
Print out the result of multiplying the two numbers together.
"""

"""
# ANSWER:
first_number = int(input("Please enter a number: "))
second_number = int(input("Please enter another number: "))

print("Your numbers multiplied by each other are", first_number * second_number, "!")
"""

"""
PROBLEM 2:
Make a python program that takes in 2 floating point numbers. Cast these to
integers and print out the result of adding them together.
"""

"""
# ANSWER:
first_number = int(float(input("Please enter a float: ")))
second_number = int(float(input("Please enter another float: ")))

print("Your numbers added to each other are", first_number + second_number, "!")
"""
