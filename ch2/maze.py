from enum import StrEnum
from typing import NamedTuple, Optional, Callable
import random
from math import sqrt
from generic_search import dfs, bfs, astar, node_to_path, Node

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
    
    def mark(self, path: list[MazeLocation]):
        for loc in path:
            self._grid[loc.row][loc.col] = Cell.PATH
        self._grid[self.start.row][self.start.col] = Cell.START
        self._grid[self.goal.row][self.goal.col] = Cell.GOAL

    def clear(self, path: list[MazeLocation]):
        for loc in path:
            self._grid[loc.row][loc.col] = Cell.EMPTY
        self._grid[self.start.row][self.start.col] = Cell.START
        self._grid[self.goal.row][self.goal.col] = Cell.GOAL

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

def euclidian_dist(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        xdist: int = ml.col - goal.col
        ydist: int = ml.row - goal.row
        return sqrt((xdist * xdist) + (ydist * ydist))
    return distance

def manhattan_dist(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        xdist: int = abs(ml.col - goal.col)
        ydist: int = abs(ml.row - goal.row)
        return (xdist + ydist)
    return distance

def main() -> None:
    m: Maze = Maze(rows=50, cols=50, goal=MazeLocation(49, 49), sparseness=0.14)
    #m: Maze = Maze()
    print(m)
    sol_1: Optional[Node[MazeLocation]] = dfs(m.start, m.goal_test, m.successors)
    if sol_1 is not None:
        print('dfs')
        path_1: list[MazeLocation] = node_to_path(sol_1)
        m.mark(path_1)
        print(m)
        m.clear(path_1)
    else:
        print('no solution found for dfs')
    
    sol_2: Optional[Node[MazeLocation]] = bfs(m.start, m.goal_test, m.successors)
    if sol_2 is not None:
        print('bfs')
        path_2: list[MazeLocation] = node_to_path(sol_2)
        m.mark(path_2)
        print(m)
        m.clear(path_2)
    else:
        print('no solution for bfs')

    sol_3: Optional[Node[MazeLocation]] = astar(m.start, m.goal_test, m.successors, manhattan_dist(m.goal))
    if sol_3 is not None:
        print('astar')
        path_3: list[MazeLocation] = node_to_path(sol_3)
        m.mark(path_3)
        print(m)
        m.clear(path_3)
    else:
        print("no solution found for astar")
if __name__ == "__main__":
    main()