from __future__ import annotations
from generic_search import bfs, dfs, astar, Node, node_to_path
from typing import Optional
# word ladder solver using search algorithms

class WLGame:
    def __init__(self, start: str, end: str, words_file: str = 'words.txt') -> None:
        if len(start) != len(end):
            raise ValueError("Start and End words should be of equal length")
        self.start = start
        self._end = end
        self._valid_words = self._get_words(words_file)
        if start not in self._valid_words or end not in self._valid_words:
            raise ValueError("Start or End word not valid")
    
    def _get_words(self, filename: str) -> set[str]:
        with open(filename) as words:
            valid_words: set[str] = set(words.read().split())    
        return valid_words
    
    def goal_seek(self, word: str) -> bool:
        return self._end == word
    
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
        return f"{self.start} -> {self._end}"

def display_solution(path: list[str]) -> None:
    for i in range(0, len(path)):
        print(path[i], end='')
        if not i == len(path)-1:
            print(" -> ", end='')

def main() -> None:
    g: WLGame = WLGame('crate', 'prime')
    count: list[int] = []
    solution: Optional[Node[str]] = bfs(g.start, g.goal_seek, g.successors, count_l=count)
    if solution is not None:
        path: list[str] = node_to_path(solution)
        display_solution(path)
        print(f"\nnum of search states: {count[0]}")

    
if __name__ == '__main__':
    main()