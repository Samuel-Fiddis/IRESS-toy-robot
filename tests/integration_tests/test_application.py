import io
import unittest
from unittest.mock import patch

from main import Application
from robot.board import Board
from robot.robot import Robot

class ApplcationTestCase(unittest.TestCase):
    def setUp(self):
        board = Board(5,5)
        robot = None
        self.app = Application(board, robot)

    @patch("sys.stdin", io.StringIO("PLACE 0,0,NORTH\nMOVE\nREPORT\nQUIT"))
    @patch('sys.stdout', new_callable = io.StringIO)
    def test_application_moving(self, stdout):
        self.app.run_cli()
        self.assertIn("0,1,NORTH", stdout.getvalue())

    @patch("sys.stdin", io.StringIO("PLACE 0,0,NORTH\nLEFT\nREPORT\nQUIT"))
    @patch('sys.stdout', new_callable = io.StringIO)
    def test_application_turning(self, stdout):
        self.app.run_cli()
        self.assertIn("0,0,WEST", stdout.getvalue())

    @patch("sys.stdin", io.StringIO("PLACE 1,2,EAST\nMOVE\nMOVE\nLEFT\nMOVE\nMOVE\nREPORT\nQUIT"))
    @patch('sys.stdout', new_callable = io.StringIO)
    def test_application_moving_and_turning(self, stdout):
        self.app.run_cli()
        self.assertIn("3,4,NORTH", stdout.getvalue())

    @patch("sys.stdin", io.StringIO("MOVE\nQUIT"))
    @patch('sys.stdout', new_callable = io.StringIO)
    def test_application_moving_without_placement(self, stdout):
        self.app.run_cli()
        self.assertIn("Initial command must place the robot with PLACE X, Y, F ", stdout.getvalue())