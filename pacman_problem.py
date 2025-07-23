
"""
TASK: Today, we will be making a 2-d pacman game that will be playable from
the terminal. We will go about this in a step-by-step process, which we will
guide you through. By the end of this, you should have a workable "pacman"-esqe
game that you can present to others!
"""

"""
Our goal is for the game board to look something like this:

. .   . . .       .
  P   . .       . .
. . .   .   . . . .
. .   .     . .
  .   . .   . .
. .         . .   .
. .   . .       .
  . .     .   .
. . .           . .
      . . .     . .

Where "." is a pellet and "P" is player.
In this game, we would like to continuously prompt the user for input (w, a, s, or d)
so they can move the player symbol and collect pellets, each giving the player a point.

We will use a class, "PacMan", to program this game. Make sure to keep testing your
program as you go!
"""


class PacMan:

    """
    Class attributes for our game; these symbols will be the same for every
    "PacMan" object that we end up making.
    """
    EMPTY = " "
    PELLET = "."
    PLAYER = "P"

    """
    I have given the instance attributes that we will need to initialize our class with:
        width: the width of the game board
        height: the height of the game board
        game_board: our empty game board
        player_location: a tuple that corresponds to the initial player position
        points: a tracker of the amount of points you have

    The game board will be a 2-d list (a list of multiple lists; essentially a grid).
    Think of it as a rectangle of indices, so a 5x5 example would be:
    grid:
    . . . . . .
    . . P . . .
    . . . . . .
    . . . . . .
    . . . . . .
    And a way we could access the point P would be grid[1][2]. (row 1, col 2)

    Remember, the way to access elements in a 2-d list is: list[index_1][index_2].
    """
    def __init__(self, width, height):
        self.board = PacMan.make_game_board(width, height)
        self.height = height
        self.width = width
        self.player_location = (1,1)
        self.points = 0


    def make_game_board(width, height):
        """
        Returns a game board where all the initial values are PacMan.EMPTY (which is " ").
        """
        board = []
        for i in range(height):
            board.append([])

        for i in range(height):
            for j in range(width):
                board[i].append(PacMan.EMPTY)
        return board


    def display_board(self):
        """
        Prints out the contents of the game board in a readable way.
        """
        for row in self.board:
            print(" ".join(row))

    """
    TODO: Make a PacMan object, with size: height = 5, width = 5.
    Access your grid and make the point at (1,1) the player symbol.
    call display board, and you should see this:

      P


    Now, change my make_game_board function to make a game board with
    every spot being a pellet and display that. You should see this:
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """

    def play(self):
        """
        Before we make the functionality of the game, let's make a game loop
        that will display the board and take in player input (that we will
        figure out how to use) every iteration of the loop. Use a while loop to
        do this; I've provided an example player input variable.

        Also, before the while loop, be sure to set the board location at
        self.player_location to "P".
        """
        self.display_board()
        player_input = input("Move with w a s d, q to quit. ")


    def move_player(self, direction):
        """
        Now, we would like to move the player based on the input given.
        One way to do that is to have a function with a direction parameter,
        taking in (w, s, a, or d) and having a dictionary corresponding to how
        the player will move based on the input. I've provided the movement
        dictionary.

        You will need to figure out how to remove the current "P" at
        player_location and update player_location depending on the input.

        Also keep in mind out of bounds errors! Use if-statements to make sure
        the player does not go out of bounds.

        After you're done with this, update your play function to allow player
        movement.
        """
        moves = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
        # player_move is a tuple corresponding to the direction the player will move
        player_move = moves[direction]

    def place_pellets(self):
        """
        Now that we have working movement, let's make a function that will place
        pellets on the game board. Feel free to place pellets any way you'd like!
        I'd recommend using loops and possibly the random module. A useful function
        is random.random(), which gives a random number between 0 and 1. You can
        also make an additional parameter in __init__, num_pellets, which will
        control the amount of pellets that will be placed on the board.

        After you're done with this, update your play function to place pellets on
        the board.
        """
        import random
        pass


    """
    TODO: Finally, update your move_player function to add a point to self.points
    whenever the player moves onto a pellet! Then update your play function to
    display points every time you go through the loop.

    If you've gotten this far, you should be done!
    """


    """
    SUPPLEMENTAL:

    If you're done early, there's some ways we can build on this problem. Implement
    whichever ones you'd like!

        Ghosts: Add a class attribute, "G", which will correspond to a ghosts. Ghosts
            will move randomly around the board, NOT destroy pellets, and will kill the
            player upon contact with it.

        Winning: Make it so the game will end when all pellets are collected!

        Walls: Add walls around (or inside) the game board that the player cannot go
            through. This will add a level of difficulty to the game.

        Move Tracker: Add a counter which tracks the number of moves the player has taken.
            You can make it so that the user only has a certain amount of moves they
            can use to win!
    """
