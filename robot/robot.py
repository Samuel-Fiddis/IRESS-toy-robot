from typing import Optional, Tuple

from robot.utils.enums import Direction, Turn, RobotError
from robot.utils.funcs import get_direction
from robot.board import Board


class Robot:
    def __init__(self):
        self.placed = False
        self.x = None
        self.y = None
        self.direction = None

    def place_robot(self, x: int, y: int, d: Direction, board: Board) -> Optional[RobotError]:
        """Attempts to place the robot on the defined board."""
        if not ((x >= 0) and (x < board.x_size) and (y >= 0) and (y < board.y_size)):
            return RobotError.PLACE_OUTSIDE_BOUNDS
        self.placed = True
        self.x = x
        self.y = y
        self.direction = d

    def turn(self, turn: Turn):
        """Turn the robot in the direction provided."""
        self.direction = Direction((self.direction.value + turn.value) % len(Direction))

    def move(self, board: Board) -> Optional[RobotError]:
        """Moves the robot one space in the direction it is facing if possible."""
        move_x, move_y = self._get_move_coords()
        if not self._can_move(move_x, move_y, board.x_size, board.y_size):
            return RobotError.WOULD_FALL
        self.x += move_x
        self.y += move_y

    def _can_move(self,
            move_x: int,
            move_y: int,
            max_x: int,
            max_y: int) -> bool:
        """Determines whether the robot can move given it's intended movement direction and the size of the board."""
        return ((self.x + move_x) >= 0) and ((self.x + move_x) < max_x) and ((self.y + move_y) >= 0) and ((self.y + move_y) < max_y)

    def _get_move_coords(self) -> Tuple[int, int]:
        """Returns the number of x and y spaces which the robot should attempt to move through."""
        if self.direction == Direction.NORTH:
            return 0, 1
        elif self.direction == Direction.EAST:
            return 1, 0
        elif self.direction == Direction.SOUTH:
            return 0, -1
        elif self.direction == Direction.WEST:
            return -1, 0

    def report(self):
        """Reports on the current location of the Robot."""
        print(f"{self.x},{self.y},{self.direction.name}")
