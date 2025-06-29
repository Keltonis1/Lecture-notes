# Homework 5 Template: Classes & Saving Data

# TODO: Create a class User with:
# name, age, student, hobbies, location

# TODO: Add methods:
# view_profile(), add_hobby(), calculate_age_in_months()

# TODO: Save/load user to file (use JSON or plain text)

# Example:
# import json
# class User:
#     def __init__(self, name, age, student, hobbies, location):
#         self.name = name
#         self.age = age
#         self.student = student
#         self.hobbies = hobbies
#         self.location = location

#     def view_profile(self):
#         print(self.__dict__)

#     def save_to_file(self, filename):
#         with open(filename, "w") as f:
#             json.dump(self.__dict__, f)

# @staticmethod
# def load_from_file(filename):
#     with open(filename, "r") as f:
#         data = json.load(f)
#         return User(**data)