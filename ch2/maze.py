from enum import StrEnum
from typing import NamedTuple
import random
#from math import sqrt
#from generic_search import dfs, bfs, node_to_path, astar, Node

class Cell(StrEnum):
    EMPTY = " "
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'

class MazeLocation(NamedTuple):
    row: int
    col: int 

class Maze:
    def __init__(self, rows: int = 10, cols: int = 10, 
                 sparseness: float = 0.2, 
                 start: MazeLocation = MazeLocation(0, 0), 
                 goal: MazeLocation = MazeLocation(9,9)) -> None:
        self._rows: int = rows
        self._cols: int = cols
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: list[list[Cell]] = [[Cell.EMPTY for _ in range(cols)] for _ in range(rows)]
        self._randomly_fill(rows, cols, sparseness)
        self._grid[start.row][start.col] = Cell.START
        self._grid[goal.row][goal.col] = Cell.GOAL

    def _randomly_fill(self, rows: int, cols: int, sparseness: float):
        for row in range(rows):
            for col in range(cols):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][col] = Cell.BLOCKED
    
    def __str__(self) -> str:
        maze: str = ''
        for row in range(self._rows):
            for col in range(self._cols):
                maze += self._grid[row][col]
            maze += '\n'
        return maze
    
    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal
    
    def successors(self, ml: MazeLocation) -> list[MazeLocation]:
        locations: list[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.col] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.col))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.col] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row-1, ml.col))
        if ml.col + 1 < self._cols and self._grid[ml.row][ml.col + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.col + 1))
        if ml.col - 1 >= 0 and self._grid[ml.row][ml.col-1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.col-1))
        return locations
            
grid: Maze = Maze(sparseness=0.0)
print(grid)
print(grid.successors(MazeLocation(5,5)))