from .MazeGenerator import MazeGenerator


def noneed() -> None:
    maze = MazeGenerator(4, 4, 4, False, {"data": None})
    print(maze)
