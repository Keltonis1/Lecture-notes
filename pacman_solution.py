class PacMan:

    """
    Class attributes for our game; these symbols will be the same for every
    "PacMan" object that we end up making.
    """
    EMPTY = " "
    PELLET = "."
    PLAYER = "P"

    """
    TODO: Initialize our class with instance attributes that we will need:
        width: the width and height of the game board
        height: the height and height of the game board
        n_pellets: the initial number of treasures on the board

        game_board: our empty game board (not an init parameter!)
        player_pos: the initial player position (not an init parameter!)

    Because 2-d lists are still unfamilliar to most of you, I've created a
    class method that you can use to make the board. Remember how to access
    elements in a 2-d list: list[index_1][index_2]
    """
    def __init__(self, width, height, n_treasures, n_traps):
        self.board = PacMan.make_game_board(width, height)
        self.height = height
        self.width = width
        self.player_location = (1,1)
        self.points = 0

    def make_game_board(width, height):
        """
        Returns a game board where all the initial values are empty (which is " ").
        """
        board = []
        for i in range(height):
            board.append([])

        for i in range(height):
            for j in range(width):
                board[i].append(PacMan.EMPTY)
        return board


    def display_board(self):
        for row in self.board:
            print(" ".join(row))


    def move_player(self, direction):
        moves = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
        dx, dy = moves[direction]

        next_location = (self.player_location[0] + dx, self.player_location[1] + dy)
        if 0 > next_location[0] or next_location[0] > self.height-1 or \
            0 > next_location[1] or next_location[1] > self.width - 1:
            print("Out of bounds")
            return

        if self.board[next_location[0]][next_location[1]] == PacMan.PELLET:
            self.points += 1

        self.board[self.player_location[0]][self.player_location[1]] = PacMan.EMPTY
        self.board[self.player_location[0] + dx][self.player_location[1] + dy] = PacMan.PLAYER

        self.player_location = (self.player_location[0] + dx, self.player_location[1] + dy)


    def place_pellets(self):
        import random
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                num = random.random()
                if num > .5:
                    self.board[i][j] = PacMan.PELLET


    def play(self):
        self.place_pellets()
        self.board[self.player_location[0]][self.player_location[1]] = "P"
        self.display_board()
        player_input = input("Move with w a s d, q to quit. ")

        while player_input != "q":
            self.move_player(player_input)
            print(f"Points: {self.points}")
            self.display_board()
            player_input = input("Move with w a s d, q to quit. ")


game = PacMan(10, 10, 5, 5)
game.play()
