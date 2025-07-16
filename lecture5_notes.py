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
# my_list = [1,2,3]
# my_list.

# class My_House():
#     description = "Something you live in"  # class attribute

#     def __init__(self, no_windows, no_doors): # init for initalize
#         self.no_windows = no_windows  # instance attributes
#         self.no_doors = no_doors
#         pass

#     def print_no_windows(self, random_number):
#         print(f"The number of windows in my house is {self.no_windows * random_number}")

#     def add_more_windows(self, number_windows):
#         self.no_windows += number_windows

# house1 = My_House(no_windows=10, no_doors=20)  # An instance of the My_House class with variables windows = 10 and doors = 20

# house1.no_windows = 20
# del house1.description
# print(house1.description)

# house1.print_no_windows(1)
# house1.add_more_windows(10)
# house1.print_no_windows(1)

# My_House.print_no_windows(house1, 1)
# My_House.add_more_windows(house1, 10)


# house2 = My_House(20, 10)
# print(house2.description)
# print(house2.no_doors)



# print(house.description)
# house.explode()

# house.description = "fat"

# print(house.description)
# print(house2.description)


# Code Demo:
# class Dog:
#     breed = "Golden retriever"
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(f"{self.name} says woof!")

#     def rename(self, name):
#         self.name = name


# my_dog = Dog("Spot")
# my_dog.name = "Rio"

# print(my_dog.name)

# my_dog.bark()




# print(my_dog.bark())


# TODO: Create a student class. Storing a student's Name, Age, Grade, and Classes


class Student():
    def __init__(self, name, age, grade, classes):
        self.name = name
        self.age = age
        self.grade = grade
        self.classes = classes

    def print(self):
        print(f"{self.name} is {self.age} and {self.grade}th grade in {self.classes}")

student_1 = Student("Bob", 14, 7, ["Math", "Science", "English"])

# student_1.name
student_1.print()

# my_dict = {
#     "fsd" : 234
# }

# my_dict["fsd"]

# Student.print(student_1)


# formatted_string = f"{15 + 5}  "















# class list(list):
#     pass

# my_list = list(range(5))
# # print(my_list)

# print(my_list.__dir__())

# my_list.name = "hi!"
# print(my_list.name)


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
