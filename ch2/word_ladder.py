from __future__ import annotations
from generic_search import bfs, astar, Node, node_to_path
from typing import Optional, Callable
# word ladder solver using search algorithms

class WLGame:
    def __init__(self, start: str, end: str, words_file: str = 'words.txt') -> None:
        if len(start) != len(end):
            raise ValueError("Start and End words should be of equal length")
        self.start = start
        self.end = end
        self._valid_words = self._get_words(words_file)
        if start not in self._valid_words or end not in self._valid_words:
            raise ValueError("Start or End word not valid")
    
    def _get_words(self, filename: str) -> set[str]:
        with open(filename) as words:
            valid_words: set[str] = set(words.read().split())    
        return valid_words
    
    def goal_seek(self, word: str) -> bool:
        return self.end == word
    
    def successors(self, word: str) -> list[str]:
        heirs: list[str] = []

        for i, v in enumerate(word):
            l_asc: int = ord(v)
            for ascii in range(97, 123): # all lower case letters
                if ascii == l_asc:
                    continue
                heirs.append(''.join([word[:i], chr(ascii), word[i+1:]]))
        return [x for x in heirs if x in self._valid_words]

    def __repr__(self) -> str:
        return f"{self.start} -> {self.end}"

def letters_diff(goal: str) -> Callable[[str], float]:
    def distance(word: str) -> float:
        return float(sum( (1 for i in range(len(goal)) if word[i] != goal[i]) ))
    return distance

def display_solution(path: list[str]) -> None:
    for i in range(0, len(path)):
        print(path[i], end='')
        if not i == len(path)-1:
            print(" -> ", end='')

def main() -> None:
    g: WLGame = WLGame('hello', 'adieu')
    count_b: list[int] = []
    count_a: list[int] = []
    solution: Optional[Node[str]] = bfs(g.start, g.goal_seek, g.successors, count_l=count_b)
    if solution is not None:
        path: list[str] = node_to_path(solution)
        display_solution(path)
        print(f"\nbfs num of search states: {count_b[0]}")

    solution_a: Optional[Node[str]] = astar(g.start, g.goal_seek, g.successors, letters_diff(g.end), count_l=count_a)
    if solution_a is not None:
        path_2: list[str] = node_to_path(solution_a)
        display_solution(path_2)
        print(f"\na* num of search states: {count_a[0]}")
if __name__ == '__main__':
    main()