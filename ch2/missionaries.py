from __future__ import annotations
from typing import Optional
from generic_search import Node, dfs, bfs, node_to_path
MAX_M: int = 2
MAX_C: int = 3

class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries
        self.wc: int = cannibals
        self.em: int = MAX_M - self.wm
        self.ec: int = MAX_C - self.wc
        self.boat: bool = boat
    
    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True
    
    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_M and self.ec == MAX_C
    
    def successors(self) -> list[MCState]:
        sucs: list[MCState] = []
        if self.boat: # boat on west bank
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc - 1, not self.boat))
            if (self.wc > 0) and (self.wm > 0):
                sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))
        else: # boat on east bank
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
            if (self.ec > 0) and (self.em > 0):
                sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))
        return [x for x in sucs if x.is_legal]

    #challenge chapter 2 excercises question 3, implement eq and hash for dfs
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MCState):
            return False
        return (self.wm == other.wm and
                self.wc == other.wc and
                self.em == other.em and
                self.ec == other.ec and
                self.boat == other.boat)
    def __hash__(self) -> int:
        return hash((self.wm, self.wc, self.em, self.ec, self.boat))
    
    def __str__(self) -> str:
        return (f"On the west bank there are {self.wm} missionaries and {self.wc} cannibals\n"
                f"On the east bank there are {self.em} missionaries and {self.ec} cannibals\n"
                f"The boat is on the {"west" if self.boat else "east"} bank")

def display_solution(path: list[MCState]) -> None:
    if len(path) == 0:
        return
    old_state: MCState = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print(f"{old_state.em - current_state.em} missionaries and {old_state.ec - current_state.ec} cannibals moved from the east to west bank")
        else:
            print(f"{old_state.wm - current_state.wm} missionaries and {old_state.wc - current_state.wc} cannibals moved from the west to east bank")
        print(current_state)
        old_state = current_state

def main() -> None:
    mcs: MCState = MCState(MAX_M, MAX_C, True)
    solution: Optional[Node[MCState]] = bfs(mcs, MCState.goal_test, MCState.successors)
    if solution is not None:
        print('------------BFS-------------\n')
        path: list[MCState] = node_to_path(solution)
        display_solution(path)

    solution2: Optional[Node[MCState]] = dfs(mcs, MCState.goal_test, MCState.successors)
    if solution2 is not None:
        print('------------DFS-------------\n')
        path2: list[MCState] = node_to_path(solution2)
        display_solution(path2)
if __name__ == '__main__':
    main()