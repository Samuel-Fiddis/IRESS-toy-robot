import io
import unittest
from unittest.mock import patch

from robot.board import Board
from main import Application
from robot.utils.enums import RobotError, Direction

class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board(5,5)
        self.app = Application(self.board)

    def test_place_robot(self):
        self.app.run_command("PLACE", "2", "2", "NORTH")
        self.assertEqual(self.app.robot.x, 2)
        self.assertEqual(self.app.robot.y, 2)
        self.assertEqual(self.app.robot.direction, Direction.NORTH)

    def test_move_robot(self):
        self.app.run_command("PLACE", "2", "2", "NORTH")
        self.app.run_command("MOVE")
        self.assertEqual(self.app.robot.x, 2)
        self.assertEqual(self.app.robot.y, 3)
        self.assertEqual(self.app.robot.direction, Direction.NORTH)

    def test_turn_robot_left(self):
        self.app.run_command("PLACE", "2", "2", "NORTH")
        self.app.run_command("LEFT")
        self.assertEqual(self.app.robot.x, 2)
        self.assertEqual(self.app.robot.y, 2)
        self.assertEqual(self.app.robot.direction, Direction.WEST)

    def test_turn_robot_right(self):
        self.app.run_command("PLACE", "2", "2", "NORTH")
        self.app.run_command("RIGHT")
        self.assertEqual(self.app.robot.x, 2)
        self.assertEqual(self.app.robot.y, 2)
        self.assertEqual(self.app.robot.direction, Direction.EAST)

    @patch('sys.stdout', new_callable = io.StringIO)
    def test_place_robot_off_board(self, stdout):
        self.app.run_command("PLACE", "5", "2", "NORTH")
        self.assertEqual(RobotError.PLACE_OUTSIDE_BOUNDS.value + '\n', stdout.getvalue())

    @patch('sys.stdout', new_callable = io.StringIO)
    def test_move_robot_off_board(self, stdout):
        self.app.run_command("PLACE", "4", "4", "NORTH")
        self.app.run_command("MOVE")
        self.assertEqual(RobotError.WOULD_FALL.value + '\n', stdout.getvalue())

    @patch('sys.stdout', new_callable = io.StringIO)
    def test_move_not_placed(self, stdout):
        self.app.run_command("MOVE")
        self.assertEqual(RobotError.NOT_PLACED.value + '\n', stdout.getvalue())