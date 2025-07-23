import random

# TODO: Use the random module to

class AdventureGame:
    """Simple terminal‑based adventure on a 2‑D list map."""

    EMPTY, WALL, PLAYER, TREASURE, TRAP, EXIT = " .P*TE"

    def __init__(self, rows=8, cols=12, n_treasures=5, n_traps=4):
        self.rows, self.cols = rows, cols
        self.map = [[AdventureGame.EMPTY for _ in range(cols)] for _ in range(rows)]
        self.player_pos = (1, 1)
        self.n_treasures = n_treasures
        self.n_traps = n_traps

        self.treasure_found = 0
        self.alive = True
        self.victory = False

    # ─────────── internal helpers ───────────
    def _place_static_walls(self):
        """Frame the playground with indestructible border walls."""
        for r in range(self.rows):
            self.map[r][0] = self.map[r][-1] = AdventureGame.WALL
        for c in range(self.cols):
            self.map[0][c] = self.map[-1][c] = AdventureGame.WALL

    def _scatter_items(self, count, kind):
        """Drop `count` items of `kind` on random empty cells."""
        placed = 0
        while placed < count:
            r = random.randint(1, self.rows - 2)
            c = random.randint(1, self.cols - 2)
            if self.map[r][c] == AdventureGame.EMPTY:
                self.map[r][c] = kind
                placed += 1

    def _place_exit(self):
        """Put the exit door somewhere along the border (but not at 0 or max indexes)."""
        edge = random.choice(
            [("top", 0), ("bottom", self.rows - 1), ("left", 0), ("right", self.cols - 1)]
        )
        if edge[0] in ("top", "bottom"):
            c = random.randint(1, self.cols - 2)
            self.map[edge[1]][c] = AdventureGame.EXIT
        else:
            r = random.randint(1, self.rows - 2)
            self.map[r][edge[1]] = AdventureGame.EXIT

    def _update_player_tile(self, new_pos=None):
        """Move player and update the map symbols."""
        r_old, c_old = self.player_pos
        self.map[r_old][c_old] = AdventureGame.EMPTY
        if new_pos:
            self.player_pos = new_pos
        r, c = self.player_pos
        self.map[r][c] = AdventureGame.PLAYER

    # ─────────── gameplay methods ───────────
    def display(self):
        for row in self.map:
            print(" ".join(row))
        print(f"Treasure: {self.treasure_found}")
        print("Move with W A S D, Q to quit")

    def _attempt_move(self, dr, dc):
        r, c = self.player_pos
        nr, nc = r + dr, c + dc
        target = self.map[nr][nc]

        if target == AdventureGame.WALL:
            print("🧱  You bump into a wall.")
            return
        if target == AdventureGame.TREASURE:
            print("💎  You found treasure!")
            self.treasure_found += 1
        elif target == AdventureGame.TRAP:
            print("💀  A hidden trap! Game over.")
            self.alive = False
            return
        elif target == AdventureGame.EXIT:
            print("🎉  You found the exit door — you win!")
            self.victory = True
            return

        self._update_player_tile((nr, nc))

    def handle_input(self, ch):
        moves = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
        if ch in moves:
            self._attempt_move(*moves[ch])
        elif ch == "q":
            self.alive = False

    def play(self):
        self._place_static_walls()
        self._scatter_items(self.n_treasures, AdventureGame.TREASURE)
        self._scatter_items(self.n_traps, AdventureGame.TRAP)
        self._place_exit()
        self._update_player_tile()
        print("=== Tiny Adventure ===")
        while self.alive and not self.victory:
            self.display()
            ch = input("→ ").strip().lower()
            self.handle_input(ch)
        print("Thanks for playing!")

game = AdventureGame()
game.play()
