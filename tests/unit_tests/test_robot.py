import unittest

from robot.board import Board
from robot.robot import Robot
from robot.utils.funcs import get_direction
from robot.utils.enums import RobotError, Direction, Turn

class RobotTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(5,5)
        self.robot = Robot()
        self.robot.place_robot(4, 2, get_direction("EAST"), self.board)

    def test_move_robot_off_board(self):
        self.assertEqual(self.robot.move(self.board), RobotError.WOULD_FALL)

    def test_turn_robot_left(self):
        self.robot.turn(Turn.LEFT)
        self.assertEqual(self.robot.direction, Direction.NORTH)
        self.robot.turn(Turn.LEFT)
        self.assertEqual(self.robot.direction, Direction.WEST)
        self.robot.turn(Turn.LEFT)
        self.assertEqual(self.robot.direction, Direction.SOUTH)
        self.robot.turn(Turn.LEFT)
        self.assertEqual(self.robot.direction, Direction.EAST)

    def test_turn_robot_right(self):
        self.robot.turn(Turn.RIGHT)
        self.assertEqual(self.robot.direction, Direction.SOUTH)
        self.robot.turn(Turn.RIGHT)
        self.assertEqual(self.robot.direction, Direction.WEST)
        self.robot.turn(Turn.RIGHT)
        self.assertEqual(self.robot.direction, Direction.NORTH)
        self.robot.turn(Turn.RIGHT)
        self.assertEqual(self.robot.direction, Direction.EAST)

    def test_move_robot(self):
        self.robot.turn(Turn.RIGHT)
        self.robot.move(self.board)
        self.assertEqual(self.robot.x, 4)
        self.assertEqual(self.robot.y, 1)
        self.assertEqual(self.robot.direction, Direction.SOUTH)

    def test_place_robot_off_board(self):
        res = self.robot.place_robot(5, 2, get_direction("EAST"), self.board)
        self.assertEqual(res, RobotError.PLACE_OUTSIDE_BOUNDS)
