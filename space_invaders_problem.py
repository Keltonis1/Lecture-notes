"""
TASK: Today, we will be making a 2-D Space Invaders game playable from
the terminal. We'll go step-by-step and guide you through each stage. By the end,
you'll have a playable shooting game that involves dodging and destroying aliens
that get closer to you every turn!
"""

"""
Our goal is for the game board to look something like this:

👾 👾   👾 👾 👾
👾     👾   👾



      ^

Where:
👾 = alien
💥 = destroyed alien
^ = your spaceship

You will move the spaceship left and right and shoot upwards to destroy aliens.
If aliens reach your row, it's game over. If you destroy them all, you win!

We will use a class, "SpaceInvaders", to build this game. Keep testing your
functions as you go!
"""

import random

class SpaceInvaders:

    ALIEN = "👾"
    EMPTY = " "
    HIT = "💥"
    PLAYER_SYMBOL = "^"

    def __init__(self, width, height, bomb_count):
        self.width = width
        self.height = height
        self.player_col = width // 2
        self.aliens = set()
        self.board = self.make_board()
        self.place_aliens(bomb_count)
        self.game_over = False
        self.win = False

    def make_board(self):
        """
        Returns a 2D list filled with EMPTY spaces.
        """
        board = []
        for i in range(self.height):
            board.append([])

        for i in range(self.height):
            for j in range(self.width):
                board[i].append(SpaceInvaders.EMPTY)
        return board

    def place_aliens(self, bomb_count):
        """
        Randomly place a number of aliens in the top two rows.
        """

    def display_board(self):
        """
        Display the board with the current player position.
        """
        for r in range(self.height):
            print(" ".join(self.board[r]))
        print("  " + " ".join(SpaceInvaders.PLAYER_SYMBOL if i == self.player_col else " " for i in range(self.width)))
        print("  " + " ".join(str(i) for i in range(self.width)))

    def move_player(self, direction):
        """
        Move the player left or right (l/r) within board boundaries.
        """

    def shoot(self):
        """
        Shoot a laser upward and destroy the first alien in the same column.
        """

    def move_aliens_down(self):
        """
        Move all aliens one row closer to the player.
        If any alien reaches the row above the player, set game_over.
        """

    def check_win(self):
        """
        Check if all aliens are destroyed. If so, set win and game_over.
        """

    def play(self):
        """
        The main game loop: display the board, ask for input,
        move or shoot, then move the aliens.
        """
        print("Welcome to Space Invaders!")
        print("Controls: 'l' = left, 'r' = right, 's' = shoot, 'q' = quit")

        while not self.game_over:
            self.display_board()
            move = input("Your action: ").strip().lower()
            if move == "l" or move == "r":
                self.move_player(move)

            elif move == "s":
                self.shoot()
                self.check_win()
                if not self.game_over:
                    self.move_aliens_down()

            elif move == "q":
                print("Game exited.")
                break

            else:
                print("Invalid input!")

        if self.win:
            print("🏆 You win! All aliens destroyed.")
        elif self.game_over:
            print("💥 Game Over! The aliens reached your base.")

if __name__ == "__main__":
    # TODO: Create a SpaceInvaders object with dimensions (7x6) and 10 aliens.
    # Then call .play() to start the game.
    game = SpaceInvaders(7, 6, 10)
    game.play()
