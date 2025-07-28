class PacMan:

    EMPTY = " "
    PELLET = "."
    PLAYER = "P"
    GHOST = "G"

    def __init__(self, width, height, num_ghosts):
        self.board = PacMan.make_game_board(width, height)
        self.height = height
        self.width = width
        self.player_location = (1,1)
        self.num_ghosts = num_ghosts
        self.ghosts = []
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
        # print(self.board)
        for row in self.board:
            print(" ".join(row))


    def move_player(self, direction):
        moves = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}

        while direction not in moves:
            direction = input("Enter a valid move: ")

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

        return (self.player_location[0] + dx, self.player_location[1] + dy)


    def place_pellets(self):
        import random
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                num = random.random()
                if num > .8:
                    self.board[i][j] = PacMan.PELLET


    def place_ghosts(self, num_ghosts):
        import random
        placed_ghosts = 0
        while num_ghosts > placed_ghosts:
            rand_col = random.randint(0, self.width) - 1
            rand_row = random.randint(0, self.height) - 1
            if self.board[rand_row][rand_col] != "G" and self.board[rand_row][rand_col] == PacMan.EMPTY:
                self.board[rand_row][rand_col] = "G"
                self.ghosts.append((rand_row, rand_col))
                placed_ghosts += 1
            else:
                continue

    def move_ghost(self, move, ghost_loc):
        dx, dy = move

        next_location = (ghost_loc[0] + dx, ghost_loc[1] + dy)
        if 0 > next_location[0] or next_location[0] > self.height-1 or \
            0 > next_location[1] or next_location[1] > self.width - 1:
            return ghost_loc
        elif self.board[next_location[0]][next_location[1]] == PacMan.GHOST:
            return ghost_loc
        elif self.board[next_location[0]][next_location[1]] == PacMan.PLAYER:
            return ghost_loc

        self.board[ghost_loc[0]][ghost_loc[1]] = PacMan.EMPTY
        self.board[ghost_loc[0] + dx][ghost_loc[1] + dy] = PacMan.GHOST

        return (ghost_loc[0] + dx, ghost_loc[1] + dy)

    def move_ghosts(self):
        import random
        for i, ghost in enumerate(self.ghosts):
            direction = random.choice([(1,0),(-1,0),(0,-1),(0,1)])
            self.ghosts[i] = self.move_ghost(direction, ghost)

    def win_check(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == ".":
                    return False
        return True


    def play(self):
        self.place_pellets()
        self.place_ghosts(self.num_ghosts)
        self.board[self.player_location[0]][self.player_location[1]] = "P"
        self.display_board()
        player_input = input("Move with w a s d, q to quit. ")

        while player_input != "q":
            self.player_location = self.move_player(player_input)
            self.move_ghosts()
            print(f"Points: {self.points}")
            self.display_board()
            if self.win_check():
                print(f"You win! Points: {self.points}")
                break

            player_input = input("Move with w a s d, q to quit. ")


game = PacMan(10, 10, 4)
game.play()
