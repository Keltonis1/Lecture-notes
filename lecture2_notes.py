####################################################
# Boolean Values                                   #
####################################################

# print(400 + 1 < 400)
# print(12 * 60 >= 8 * 90)
# print(5 == 5.0)

# print(12+7 != 3+17)

# print(bool(0)) # False!
# print(bool(15)) # True!


# TODO: What will these examples print out?

time = 10 # AM
booleanTime = time < 11
food_in_fridge = False

# print(booleanTime and food_in_fridge)
# print(time < 11 or food_in_fridge)
# print(time < 11 and not food_in_fridge)


####################################################
# Conditionals!                                    #
####################################################

# is_raining = False
# is_sunny = False

# if is_raining or is_sunny:
#     print("Umbrella")
# print("Outside statement")


# Conditionals example

food_in_fridge = False

# if not food_in_fridge:
#     print("Go buy some food!")


"""
TODO: Write a program that asks the user for a password. If the password matches
      a different variable named "password", print "access granted". If password doesnn't
      match, print "access denied".
"""

# password = "password"
# user_input = str(input("Enter a password: "))

# if user_input == password:
#     print("access granted!")
# elif len(user_input) < 2:
#     print("password is too short")
# else:
#     print("access denied!")


"""
TODO: If it's raining and it's July 5th, print "I'm not going outside." Otherwise,
      print "I'll go outside!"
"""

it_is_raining = False
todays_date = "July 5"

# if it_is_raining and todays_date == "July 5":
#     print("I'm not going outside")
# else:
#     print("I'll go outside")

# TODO: Predict what would happen if age = 10, 18, or 30

# age = 30
# # if todays_date == "July 5":
# #     print("Not in chain")

# if age > 22:
#     print('You can be a lecturer')
#     # print("In chain")
# if age > 16:
#     print('You can be a teaching assistant')
#     # print("In chain")
# else:
#    print('Go study! You are a student')
# #    print("In chain")


# TODO: Coding rock paper scissors using input and if-statements!

# player_1 = input("Enter your move: ")
# player_2 = input("Enter your move: ")

# if player_1 == "Rock" and player_2 == "Rock":
#     print("That is a tie. Go again")

# if player_1 == "Rock":
#     if player_2 == "Rock":
#         print("That is a tie. Go again")
#     elif player_2 == "Paper":
#         print("Player 2 wins")
#     else:
#         print("Player 1 wins")
# elif player_1 == "Paper":
#     if player_2 == "Rock":
#         print("Player 1 wins")
#     elif player_2 == "Scissors":
#         print("Player 2 wins")
#     else:
#         print("That is a tie. Go again")
# else: # player_1 == "Scissors"
#     if player_2 == "Paper":
#         print("Player 1 wins")
#     elif player_2 == "Rock":
#         print("Player 2 wins")
#     else:
#         print("That is a tie. Go again")


a,b = 5,10

a = 5
b = 10

min = a if a < b else b

if a < b:
    min = a
else:
    min = b

# print(min)


is_raining = True
has_umbrella = True

# if it is raining and you have an umbrella, print "good to go"
# otherwise, print "you are soaked"


# status = "good to go" if is_raining and has_umbrella else "you are soaked"

# if is_raining and has_umbrella:
#     print("good to go")
# else:
#     print("you are soaked")

# print(status)





####################################################
# String Indexing                                  #
####################################################


"fsdjaldkjfoe12903!@&*(#@)"

# TODO: Look through these examples

name = "Frederick" # the length of frederick is 9

# print(name[0]) # First element
# print(name[1]) # Second element
# print(name[0:]) # First element onward
# print(name[1:]) # Second element onward
# print(name[::]) # same as name. Entire string
# print(name[0:9:1])
# name[:]  # same as name. Entire string
# name[0:3] # Elements 0, 1 and 2
# name[:3] # Elements 0, 1 and 2 same as above
# print(name[0:9:1]) # Same as name or name[::]. Entire string. No element skipped
# print(name[0::2]) # Skip every other element
# name[::2] # Skip every other element same as above
# print(name[::-1]) # reverse string
# print(name[5::-1]) # reverse starting at 5
# print(name[-1]) # last element
# print(name[-2]) # second last element
# print(name[-3:]) # last 3 elementss

# my_string = "A string"
# print(my_string[0::3])


fruit = "banana"
# print(fruit[1:5]) # What will this print?
# print(fruit[:5])
# print(fruit[::-1])
# print(fruit[0:5:2]) # same as string[:5:2]

# fruit[::]

# fruit[0:6:1]

# print(len(fruit))


song = """ it is
raining outside
"""
# print(song)

# print(len(name))
# print(len(fruit))

# print(f"I have {fruit}!")
# print(f"My name is {name}!")


name = "nick"
ten_nicks = "nick" * 10

new_name = "james"
names_together = name + new_name

# print(names_together)

name = "Eric"
age = 74

# print(f"My name is {name} and I am {age} years old.")


# TODO: Use f-strings to print out the sum of 2 values in a string format:
#       "I have <apples> apples and <oranges> oranges, which is <apples +
#       <oranges> fruits!"

apples = 5
oranges = 6
# print(f"I have {apples} apples and {oranges} oranges, which is {apples + oranges} fruits!")
# print(f"I have", apples, f"apples and {oranges} oranges, which is {apples + oranges} fruits!")




"""
TODO: Pair coding assignment:
Get user input to any date in MM/DD/YYYY format. Use if statements and
string slicing to determine whether this date is before or after today's date.
"""

todays_date = "07/05/2025"      # enter today’s date here

# user_input = input("Enter any date in MM/DD/YYYY format") # "MM/DD/YYYY"

# this_year = int(todays_date[6:10])
# user_year = int(user_input[6:10]) # 2026

# if user_year > this_year:
#     print("This is after")
# elif user_year < this_year:
#     print("This is before")




####################################################
# Lists                                            #
####################################################

# BASIC LIST STRUCTURE
thislist = ["apple", "banana", "cherry"]
# print(thislist[0])
# print(thislist[1])
# print(thislist[2])
# print(thislist[0:])

# thislist[0] = 1
# print(thislist)


# a_string = "hello!"
# a_string[0] = 2


# TODO: Experiment with list slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[0:2])
# print(thislist[:4])
# print(thislist[:4:2])
# print(len(thislist))




# TODO: add two people to the list, Jeremy and Jackson, with append, extend and insert

people = ["James", "Jackie", "Jason"]
# people.append("Jeremy")
# people.append("Jackson")

# print(people)
new_list = ["Jeremy", "Jackson"]

people.extend(new_list)
print(people)
