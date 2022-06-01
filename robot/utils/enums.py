from enum import Enum, unique, auto
import re

@unique
class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


@unique
class Turn(Enum):
    LEFT = -1
    RIGHT = 1


@unique
class Command(Enum):
    HELP = auto()
    PLACE = auto()
    MOVE = auto()
    LEFT = auto()
    RIGHT = auto()
    REPORT = auto()
    QUIT = auto()


@unique
class RobotError(Enum):
    NOT_PLACED = "Robot is not yet placed on the board."
    PLACE_OUTSIDE_BOUNDS = "Cannont place robot outside of board boundaries."
    WOULD_FALL = "Cannot move Robot. It would fall from the board!"

INITIAL_COMMANDS = [Command.HELP, Command.PLACE, Command.QUIT]

COMMAND_REGEX = {
    Command.HELP: f"{Command.HELP.name}$",
    Command.PLACE: f'PLACE\s+\d+,\s?\d+,\s?({"|".join([dirc.name for dirc in Direction])})$',
    Command.MOVE: f"{Command.MOVE.name}$",
    Command.LEFT: f"{Command.LEFT.name}$",
    Command.RIGHT: f"{Command.RIGHT.name}$",
    Command.REPORT: f"{Command.REPORT.name}$",
    Command.QUIT: f"{Command.QUIT.name}$"
}

COMMAND_PARAMETERS = {
    Command.HELP: [],
    Command.PLACE: ["Integer", "Integer", "Direction"],
    Command.MOVE: [],
    Command.LEFT: [],
    Command.RIGHT: [],
    Command.REPORT: [],
    Command.QUIT: []
}
