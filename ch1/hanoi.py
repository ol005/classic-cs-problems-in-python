# towers of hanoi solver

from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: list[T] = []
    
    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    
    def get_list(self) -> list[T]:
        return self._container

    def __repr__(self) -> str:
        return repr(self._container)

def print_towers(towers: list[Stack[int]], n: int) -> None:
    
    for i in range(n-1, -1, -1):
        for twr in towers:
            li = twr.get_list()
            if len(li) > i:
                print(f'| {li[i]} |', end='')
            else:
                print('|  |', end='')
        print('')
                
def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:

    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)

# 1.7 challenge exercise question 3
# implement iter solution for tower of hanoi and variable number of towers
def hanoi_iter(towers: list[Stack[int]], discs: int, num_towers: int) -> None:
    smallest_move: bool = True
    start: Stack[int] = towers[0]
    end: Stack[int] = towers[num_towers-1]

    #end condition:
    while(len(end) < discs):
        if(smallest_move):
            
    pass

    



def main():
    num_discs: int = 6
    num_towers: int = 3
    towers: list[Stack[int]] = []
    for i in range(num_towers):
        towers.append(Stack())


    for i in range(num_discs, 0, -1):
        towers[0].push(i)

    print_towers(towers, num_discs)
    #hanoi(twr_a, twr_c, twr_b, num_discs)


if __name__ == "__main__":
    main()

