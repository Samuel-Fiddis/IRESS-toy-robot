import re
from typing import Optional, Sequence, Tuple

from robot.utils.enums import Command, Direction


def get_command(command: str) -> Optional[Command]:
    try:
        return Command[command]
    except KeyError:
        print("Command not recognised.")


def get_direction(direction: str) -> Optional[Direction]:
    try:
        return Direction[direction]
    except KeyError:
        print("Direction not recognised.")


def get_input() -> Tuple[str, Sequence[str]]:
    vars_string = input(">> ")
    return vars_string, re.split('\\W+', vars_string)


def display_options() -> None:
    print("""Commands:
        - PLACE X, Y, F: will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0)
        can be considered to be the SOUTH WEST most corner. It is required that the first command to the robot is a PLACE
        command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The
        application will discard all other commands until a valid PLACE command has been executed.
        - MOVE: will move the toy robot one unit forward in the direction it is currently facing.
        - LEFT and RIGHT: will rotate the robot 90 degrees in the specified direction without changing the position of the
        robot.
        - REPORT: will announce the X,Y and F of the robot.
        - QUIT: will quit the application.""")
