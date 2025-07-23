
"""
TASK: Today, we will be making a 2-d adventure game that will be playable from
the terminal. We will go about this in a step-by-step process, which we will
guide you through. By the end of this, you should have a workable "dungeon"-esqe
game that you can present to others!
"""

"""
Our goal is for the game board to look something like this:
    . . . . . . . . . . . .
    . P                   .
    . *   T           T   E
    .   *     * T *       .
    .           *         .
    .                     .
    .           T         .
    . . . . . . . . . . . .
Where "." is a wall, "P" is player, "T" is trap, "E" is exit, and "*" is treasure.
In this game, we would like to continuously prompt the user for input (w, a, s, or d)
so they can move the player symbol, collect treasure, and eventually exit.

We will use a class, "AdventureGame", to program this game. Make sure to keep testing your
program as you go!
"""


class AdventureGame:

    """
    Class attributes for our game; these symbols will be the same for every
    "AdventureGame" object that we end up making.
    """
    EMPTY = " "
    WALL = "."
    TREASURE = "*"
    PLAYER = "P"
    TRAP = "T"
    EXIT = "E"

    """
    TODO: Initialize our class with instance attributes that we will need:
        width: the width and height of the game board
        height: the height and height of the game board
        n_treasures: the initial number of treasures on the board
        n_traps: the number of traps that will be on the board
        game_board: our empty game board
        player_pos: the initial player position

    Because 2-d lists are still unfamilliar to most of you, I've created a
    class method that you can use to make the board.
    """
    def __init__(self):
        # TODO: initialize all
        # self.board = AdventureGame.make_game_board(width, height)
        pass


    def make_game_board(width, height):
        """
        Returns a game board where all the initial values are empty (which is " ").
        """
        board = []
        for i in range(height):
            board.append([])

        for i in range(height):
            for j in range(width):
                board[i].append(AdventureGame.EMPTY)
        return board


    def display_board(self):
        for row in self.board:
            print(" ".join(row))
