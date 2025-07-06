####################################################
# Lists, Continued                                 #
####################################################

# TODO: add two people to the list, Jeremy and Jackson, with append, extend and insert

people = ["James", "Jackie", "Jason"]

# people.append("Jeremy")
# people.append("Jackson")
# print(people)

# new_list = ["Jeremy", "Jackson"]
# people.extend(new_list)
# print(people)

# people.insert(3, "Jeremy")
# people.insert(4, "Jackson")
# print(people)


# TODO: Now remove James from the list with pop() and remove() and print it
# people.pop(0)
# print(people)

# people.remove("James")
# print(people)


# TODO: Class exercise: add zero to the start of the list

nums = [1,2,3,4]

# nums.insert(0, 0)
# print(nums)


# TODO: Make a 2-d array

fruits = [
    ["Banana", "Cherry"],
    ["Apple", "Guava"]
]
# print(fruits[0][0]) # Banana
# print(fruits[1][0]) # Apple
# print(fruits[0][1]) # Cherry
# print(fruits[1][1]) # Guava




# ALIASING WARNING
fruits = ["apple", "banana", "cherry"]
new_list = fruits

new_list[1] = "apple"
# print(new_list)
# print(fruits)


####################################################
# Tuples                                           #
####################################################

# BASIC STRUCTURE
my_tuple = (1,2,3)
new_tuple = my_tuple[:2]

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


####################################################
# Dictionaries                                     #
####################################################

"""
BASIC STRUCTURE:

dict = {}

value = 5
dict["index"] = value
"""


# TODO: Populate phone numbers dictionary with names corresponding to numbers

phone_numbers = {}






####################################################
# While Loops                                      #
####################################################

"""
BASIC STRUCTURE:
while <boolean expression is true>:
    repeat this code body
"""

# Most simple while loop:

# while True:
#     print(":)")


# print("hi")
# print("hi")
# print("hi")
# print("hi")
# print("hi")

# TODO: Code a while loop so you don't need to write this five times!


# TODO: Analyze this simple while loop. What does it do? Type in slido

# while True:
#     user_input = input("Type 'exit' to quit: ")
#     if user_input == "exit":
#         break
#     print("You typed:", user_input)


"""
TODO: Modify your rock paper scissors game from last class such that you can restart,
      or quit after each round. Make a variable to track how many times players
      1 and 2 have won, and print it out after each round.
"""

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


####################################################
# For Loops                                        #
####################################################

# TODO: Make a for loop that modifies this list to add five to each element in it.

numbers = [1,2,3,4,5,6]


# TODO: Make a for loop that prints the numbers 1 through 10

for i in range(10):
    print(i)


# TODO: Write this in a while loop format

# ind = 0
# while ind < 10:
#     print(ind)
#     ind += 1



# TODO: Use the provided for loop and the continue keyword, print every other number using
#       up until the number 20

# for i in range(100):


# TODO: Do the same thing just by calling range and using a different step



####################################################
# Break and Continue                               #
####################################################


"""
Pair Programming: Tic Tac Toe

"""
