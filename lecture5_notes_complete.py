
# Lecture 2: Classes, Inheritance, File I/O
# Time: 2 hours
# Structure: 60% Slides + Code Demos, 40% Pair Programming

# Section 1: Classes
## Description:
# Introduce Object-Oriented Programming with classes and objects.

## Key Concepts:
# - class and __init__
# - self keyword
# - instance variables and methods

## Code Demo:
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

d = Dog("Buddy")
print(d.bark())

## Additional Example:
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

acct = BankAccount("Alice", 100)
print(acct.deposit(50))
print(acct.withdraw(200))

# Section 2: Inheritance
## Description:
# Teach how to create child classes from parent classes.

## Key Concepts:
# - Inheriting with class SubClass(ParentClass)
# - Overriding methods
# - super()

## Code Demo:
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

print(Dog().speak())

## Exercises:
# Create a `Vehicle` class and extend it into `Car` and `Bike`.

class Vehicle:
    wheel_count=0
    def __init__(self, brand, wheel_count):
        self.brand = brand

    def start(self):
        return f"{self.brand} is starting."

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        super().wheel_count = 4

    def start(self):
        return f"{self.brand} car is zooming off."

class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
        super().wheel_count = 2

    def start(self):
        return f"{self.brand} is parking my bike."

my_vehicle = Vehicle()
my_car = Car("Toyota")
my_bike = Bike("Huffy")
print(my_vehicle.start())
print(my_car.start())
print(my_bike.start())

## Exercises:
# Create a `Shape` class and inherit `Rectangle` and `Circle` with methods to compute area.

# Section 3: File I/O
## Description:
# Read and write to text files using Python.

## Key Concepts:
# - open(), read(), write(), close()
# - Using with open() for context management

## Code Demo:
with open("demo.txt", "w") as f:
    f.write("Hello, file!")

with open("demo.txt", "r") as f:
    content = f.read()
    print(content)

## Additional Example:
def save_game_log(player_name, score):
    with open("game_log.txt", "a") as log:
        log.write(f"{player_name} scored {score}\n")

save_game_log("Alice", 5)

## Exercises:
# Write a function that reads a file and returns the number of lines.

# Pair Programming Project:
## Task:
# Refactor the guessing game from lecture 1 into a class:
# - Class: GuessingGame
# - Method: play(), save_result()
# - Write results to a file named `results.txt`
