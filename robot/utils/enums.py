from enum import Enum, unique, auto


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
    NOT_PLACED = auto()
    PLACE_OUTSIDE_BOUNDS = auto()
    WOULD_FALL = auto()


ERROR_MESSAGES = {
    RobotError.NOT_PLACED: "Robot is not yet placed on the board.",
    RobotError.PLACE_OUTSIDE_BOUNDS: "Cannont place robot outside of board boundaries.",
    RobotError.WOULD_FALL: "Cannot move Robot. It would fall from the board!"}

INITIAL_COMMANDS = [Command.HELP, Command.PLACE, Command.QUIT]

COMMAND_PARAMETERS = {
    Command.HELP: [],
    Command.PLACE: ["Integer", "Integer", "Direction"],
    Command.MOVE: [],
    Command.LEFT: [],
    Command.RIGHT: [],
    Command.REPORT: [],
    Command.QUIT: []
}
