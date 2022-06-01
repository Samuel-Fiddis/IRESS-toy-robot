"""Toy Robot Application.

A Toy Robot application produced for an technical challenge at IRESS.
Author: Sam Fiddis
email: sam.fiddis@gmail.com"""

from typing import Optional, Sequence
from pyhocon import ConfigFactory
import re

from robot.utils.enums import Command, COMMAND_PARAMETERS, COMMAND_REGEX, ERROR_MESSAGES, INITIAL_COMMANDS, RobotError, Direction, Turn
from robot.utils.funcs import get_command, get_direction, get_input, display_options
from robot.robot import Robot
from robot.board import Board


class Application:
    def __init__(self, board: Board, robot: Optional[Robot] = None) -> None:
        self.board = board
        self.robot = robot
        if robot is None:
            self.robot = Robot()
        self.running = False

    def run_cli(self) -> None:
        """Runs the application in client interface mode."""
        print(f"Toy Robot Client Interface.\nBoard size is {self.board.x_size} x {self.board.y_size}.\nFor help type HELP. To quit type QUIT.")
        self.running = True
        self._wait_till_robot_placement()

        while(self.running):
            vars_string, vars = get_input()
            if self.check_command_inputs(vars_string):
                self.run_command(*vars)

    def _wait_till_robot_placement(self) -> None:
        """Waits till the robot has been placed on the board before allowing other commands."""
        while(self.robot.placed == False and self.running):
            vars_string, vars = get_input()
            if (get_command(vars[0]) not in INITIAL_COMMANDS):
                print(
                    f"""Initial command must place the robot with PLACE X, Y, F where:
                X is between 0 and {self.board.x_size - 1}
                Y is between 0 and {self.board.y_size - 1}
                F is one of {", ".join([d.name for d in Direction])}""")
                continue
            elif self.check_command_inputs(vars_string):
                self.run_command(*vars)

    def check_command_inputs(self, vars_string: str) -> bool:
        """Performs an initial check on the passed commands to determine if they satisfy constraints."""
        vars = re.split('\\W+', vars_string)
        if len(vars) == 0:
            return False
        command = get_command(vars[0])
        if command:
            if not re.match(COMMAND_REGEX[command], vars_string):
                print(f"Command {command.name} requires {len(COMMAND_PARAMETERS[command])} variables", end='')
                if len(COMMAND_PARAMETERS[command]) > 0:
                    print(" of types " + ", ".join(COMMAND_PARAMETERS[command]), end='')
                print(". For help type HELP.")
                return False
            else:
                return True
        return False

    def run_command(self,
            command: str,
            x: Optional[str] = None,
            y: Optional[str] = None,
            d: Optional[str] = None) -> None:
        """Runs the given command with optional arguments for the PLACE command."""
        command = get_command(command)
        res = None
        if command == Command.HELP:
            display_options()
        elif command == Command.QUIT:
            self.running = False
        elif command == Command.PLACE:
            res = self.robot.place_robot(int(x), int(y), get_direction(d), self.board)
        elif not self.robot.placed:
            res = RobotError.NOT_PLACED
        elif command == Command.MOVE:
            res = self.robot.move(self.board)
        elif command == Command.LEFT:
            self.robot.turn(Turn.LEFT)
        elif command == Command.RIGHT:
            self.robot.turn(Turn.RIGHT)
        elif command == Command.REPORT:
            self.robot.report()

        if res:
            print(ERROR_MESSAGES[res])


if __name__ == "__main__":
    config = ConfigFactory.parse_file("default.conf")
    board = Board(int(config["board"]["x_size"]), int(config["board"]["y_size"]))
    app = Application(board)
    app.run_cli()
