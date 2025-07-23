#!/usr/bin/env python3
"""
Text‑mode Space Invaders — frame‑by‑frame.
Controls per turn (enter one key then press ↵ Enter):

    a   move ship left
    d   move ship right
    f   fire laser
    s   stay (no action)
    q   quit

Aliens march sideways, dropping a row whenever they hit a wall.
Win: destroy every alien.  Lose: an alien reaches your row.
"""

import sys
import random


class SpaceInvaders:
    ALIEN      = "W"   # enemy sprite
    SHIP       = "A"   # your ship
    BULLET     = "|"   # laser shot
    EMPTY      = " "   # blank cell

    def __init__(self, rows=14, cols=25, alien_rows=3, alien_cols=8):
        self.rows, self.cols = rows, cols

        # ------ entities ------
        # player ship starts bottom‑center
        self.ship_col = cols // 2
        # aliens in formation (top‑left corner offset)
        self.aliens = {
            (r, c)
            for r in range(alien_rows)
            for c in range(alien_cols)
        }
        self.alien_offset_r = 1
        self.alien_offset_c = 2
        self.alien_dir = 1  # +1 right, −1 left
        # bullets are (row, col)
        self.bullets = set()

        self.turn = 0
        self.game_over = False
        self.victory = False

    # ─────────── rendering ───────────
    def _grid(self):
        grid = [[self.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]
        # place aliens
        for ar, ac in self.aliens:
            r = self.alien_offset_r + ar
            c = self.alien_offset_c + ac
            if 0 <= r < self.rows and 0 <= c < self.cols:
                grid[r][c] = self.ALIEN
        # place bullets
        for br, bc in self.bullets:
            if 0 <= br < self.rows:
                grid[br][bc] = self.BULLET
        # place ship
        grid[self.rows - 1][self.ship_col] = self.SHIP
        return grid

    def display(self):
        print("\n" * 3)  # clear-ish
        print(f"Turn {self.turn} — Aliens left: {len(self.aliens)}")
        border = "+" + "-" * self.cols + "+"
        print(border)
        for row in self._grid():
            print("|" + "".join(row) + "|")
        print(border)
        print("a=left  d=right  f=fire  s=stay  q=quit")

    # ─────────── player action ───────────
    def handle_input(self, cmd: str):
        cmd = cmd.lower()
        if cmd == "a" and self.ship_col > 0:
            self.ship_col -= 1
        elif cmd == "d" and self.ship_col < self.cols - 1:
            self.ship_col += 1
        elif cmd == "f":
            # shoot if not already a bullet at ship position
            self.bullets.add((self.rows - 2, self.ship_col))
        elif cmd == "q":
            self.game_over = True
        # any other key = stay

    # ─────────── game logic ───────────
    def _move_bullets(self):
        next_bullets = set()
        for br, bc in self.bullets:
            br -= 1  # move up
            if br < 0:
                continue
            # check collision with aliens
            for ar, ac in list(self.aliens):
                real_r = self.alien_offset_r + ar
                real_c = self.alien_offset_c + ac
                if (br, bc) == (real_r, real_c):
                    self.aliens.remove((ar, ac))
                    break
            else:
                next_bullets.add((br, bc))
        self.bullets = next_bullets

    def _move_aliens(self):
        # check if next horizontal step hits wall
        next_offset_c = self.alien_offset_c + self.alien_dir
        hit_wall = any(
            not (0 <= next_offset_c + ac < self.cols)
            for _, ac in self.aliens
        )
        if hit_wall:
            # descend one row & reverse
            self.alien_offset_r += 1
            self.alien_dir *= -1
            # after moving down, immediate loss check
        else:
            self.alien_offset_c = next_offset_c

    def _loss_check(self):
        # alien reached player's row?
        for ar, ac in self.aliens:
            if self.alien_offset_r + ar >= self.rows - 1:
                self.game_over = True
                return "Aliens have landed! You lose."
        return None

    def _win_check(self):
        if not self.aliens:
            self.victory = True
            self.game_over = True
            return "All aliens destroyed! You win!"
        return None

    def step(self, cmd: str):
        if self.game_over:
            return
        self.turn += 1
        self.handle_input(cmd)
        self._move_bullets()
        self._move_aliens()
        # check losses / wins
        msg = self._loss_check()
        if msg:
            print(msg)
            return
        msg = self._win_check()
        if msg:
            print(msg)

    # ─────────── outer loop ───────────
    def play(self):
        while not self.game_over:
            self.display()
            cmd = input("> ").strip()[:1] or "s"
            self.step(cmd)
        # final board
        self.display()
        if self.victory:
            print("🎉  Victory!")
        else:
            print("💀  Game over.")


def main():
    game = SpaceInvaders()
    game.play()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
