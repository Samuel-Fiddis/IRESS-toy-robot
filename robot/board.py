import numpy as np


class Board:
    def __init__(self, x: int, y: int) -> None:
        """Creates a board of size x, y."""
        self.x_size = x
        self.y_size = y
        self.table = np.zeros((x, y), dtype=int)

    def place_obstacle(self, x: int, y: int) -> None:
        """Places and obstacle on the board at position x, y."""
        self.table[x][y] = 1

    def check_for_obstacle(self, x: int, y: int) -> bool:
        """Checks for an obstacle on the board at position x, y."""
        return bool(self.table[x][y])
