####################################################
# Boolean Values                                   #
####################################################

# print(400 + 1 < 400)
# print(12 * 60 >= 8 * 90)
# print(5 == 5.0)

# print(bool(0)) # False!
# print(bool(1)) # True!


# TODO: What will these examples print out?

time = 10 # AM
food_in_fridge = False

# print(time < 11 and food_in_fridge)
# print(time < 11 or food_in_fridge)
# print(time < 11 and not food_in_fridge)


####################################################
# Conditionals!                                    #
####################################################

# Conditionals example

food_in_fridge = False

# if not food_in_fridge:
#     print("Go buy some food!")


"""
TODO: Write a program that asks the user for a password. If the password matches
      a different variable named "password", print "access granted"
"""

password = "password"
# user_input =


"""
TODO: If it's raining and it's July 5th, print "I'm not going outside." Otherwise,
      print "I'll go outside!"
"""

it_is_raining = False
todays_date = "July 5"


# TODO: Predict what would happen if age = 10, 18, or 30

# age = 22

# if age > 22:
#     print('You can be a lecturer')
# elif age > 16:
#     print('You can be a teaching assistant')
# else:
#    print('Go study! You are a student')


# TODO: Coding rock paper scissors using input and if-statements!

# player_1 = input("Enter your move")



####################################################
# String Indexing                                  #
####################################################

# TODO: Look through these examples

name = "Frederick"

# name[0] # First element
# name[1] # Second element
# name[0:] # First element onward
# name[1:] # Second element onward
# name[::]  # same as name. Entire string
# name[:]  # same as name. Entire string
# name[0:3] # Elements 0, 1 and 2
# name[:3] # Elements 0, 1 and 2 same as above
# name[0::1] # Same as name or name[::]. Entire string. No element skipped
# name[0::2] # Skip every other element
# name[::2] # Skip every other element same as above
# name[::-1] # reverse string
# name[5::-1] # reverse starting at 5
# name[-1] # last element
# name[-2] # second last element
# name[-3:] # last 3 elementss


fruit = "banana"
# print(string[1:5]) # What will this print?
# print(string[:5])
# print(string[-1])
# print(string[0:5:2]) # same as string[:5:2] and string[::2]



# print(len(name))
# print(len(fruit))

# print(f"I have {fruit}!")
# print(f"My name is {name}!")

# TODO: Pair coding: Find someone's age! Use f-strings to make a print statement

todays_date = "06/08/2025"      # enter today’s date here
todays_day = todays_date[0:2]
todays_month = todays_date[3:5]
todays_year = todays_date[6:]

# user_input = input("enter your birthday")



####################################################
# Lists                                            #
####################################################

# BASIC LIST STRUCTURE
thislist = ["apple", "banana", "cherry"]
# print(thislist[0])
# print(thislist[1])
# print(thislist[2])

# thislist[0] = 1
# print(thislist[0])





# TODO: Experiment with list slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[0:2])
# print(thislist[:4])
# print(thislist[:4:2])
# print(len(thislist))



# TODO: add two people to the list, Jeremy and Jackson, with append, extend and insert

people = ["James", "Jackie", "Jason"]

# TODO: Now remove James from the list with pop() and remove() and print it




# TODO: add zero to the start of the list

ls = [1,2,3,4]




# TODO: Make a 2-d array
fruits = [
    ["Banana", "Cherry"],
    ["Apple", "Guava"]
]
# print(fruits[0][0]) # Banana
# print(fruits[1][0]) # Apple
# print(fruits[0][1]) # Cherry
# print(fruits[1][1]) # Guava

new_list = fruits


####################################################
# Tuples                                           #
####################################################

# my_tuple = (1,2,3)
# my_tuple[1] = 2


# TODO: Experiment with lists and tuples. Find out what is and isn't possible

# a = ['hello', "friend", '!']  # a list with 3 elements
# len(a)
# a[0]
# a[2] = '!!!'

# a = ('hello', "friend", '!')
# len(a)
# a[0]
# a[2] = '!!!'

# What if a[2] is a list? Try this:

# a = ('hello', "friend", ['!'])
# len(a)
# a[0]
# a[2][0] = '!!!'
# print(a[2])


# TODO: Make a list of tuples, with info on first and last names, and age:
"""
James Madison, 15
Jackie Brown, 24
Jason Chen, 23
Jeremy Chen, 18
Jackson Coll, 30
"""

# TODO: Use sort() to sort the list alphabetically by last name


# TODO: Make that a dictionary, with last name corresponding to first name and age.




# Tic tac toe? with pre-written code for pair programming?? for the loops lecturex
