from MazeGenerator import MazeGenerator
wall_values = {"north": 1, "east": 2, "south": 4, "west": 8}


class Cell:
    def __init__(self) -> None:
        self.walls = 15

    def has_wall(self, direction: str) -> int:
        return (self.walls & wall_values[direction])

    def open_wall(self, direction: str) -> None:
        if self.has_wall(direction):
            self.walls -= wall_values[direction]
        else:
            raise ValueError(
                f"The cell doesnt have this wall: {direction}")

    def close_wall(self, direction: str) -> None:
        if not self.has_wall(direction):
            self.walls += wall_values[direction]
        else:
            raise ValueError(
                f"The cell already has the wall closed : {direction}")


if __name__ == "__main__":
    maze = MazeGenerator(9, 9, None, False)
    maze.forty_two_cells()
    maze.generate()
    maze.set_entry_exit()
    path = maze.find_shortest_path()
    maze.display(path)
